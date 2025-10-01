from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

# Charger dataset exemple
X, y = load_iris(return_X_y=True)

# Entraîner un modèle simple
clf = RandomForestClassifier().fit(X, y)

# Sauvegarder
Path("models").mkdir(exist_ok=True)
joblib.dump(clf, "models/model.pkl")
print("✅ Modèle sauvegardé dans models/model.pkl")
