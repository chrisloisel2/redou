import joblib
from pathlib import Path
from functools import lru_cache

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "model.pkl"

@lru_cache(maxsize=1)
def get_model():
    return joblib.load(MODEL_PATH)

def predict(X):
    model = get_model()
    return model.predict(X)
