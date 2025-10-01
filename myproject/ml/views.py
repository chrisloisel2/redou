import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .model_store import predict

@csrf_exempt
def predict_view(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Utilise POST avec JSON: {\"inputs\": [[...]]}")
    try:
        data = json.loads(request.body)
        X = data.get("inputs")
        y = predict(X)
        return JsonResponse({"predictions": y.tolist()})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)
