# Projet Django IA Minimal

Ce projet est un exemple **minimaliste** d'intégration d'un modèle de
Machine Learning dans un projet **Django**.\
Il contient :

-   Un script Python pour **entraîner** un modèle et le sauvegarder
    (`train_model.py`).
-   Un projet Django avec **une seule route** `/predict` qui permet de
    faire des prédictions.
-   Une organisation simple et claire pour comprendre le fonctionnement.

------------------------------------------------------------------------

## ⚙️ Installation

1.  **Cloner le projet et se placer dans le dossier :**

    ``` bash
    git clone <repo-url>
    cd myproject
    ```

2.  **Créer un environnement virtuel et installer les dépendances :**

    ``` bash
    python3 -m venv .venv
    source .venv/bin/activate   # Linux/Mac
    # .\.venv\Scripts\activate  # Windows PowerShell

    pip install -r requirements.txt
    ```

------------------------------------------------------------------------

## 🤖 Entraîner le modèle

Le fichier `train_model.py` sert à entraîner un modèle
**RandomForestClassifier** sur le dataset Iris (inclus avec
scikit-learn).\
Il sauvegarde ensuite le modèle entraîné dans `models/model.pkl`.

``` bash
python train_model.py
```

Une fois exécuté, vous verrez :

    ✅ Modèle sauvegardé dans models/model.pkl

------------------------------------------------------------------------

## 🧩 Structure du projet

    myproject/
      manage.py
      config/
        settings.py
        urls.py
      ml/
        views.py
        model_store.py
      train_model.py   <-- script d’entraînement
      models/
        model.pkl      <-- modèle entraîné

-   `train_model.py` : Entraîne et sauvegarde le modèle.
-   `ml/model_store.py` : Charge le modèle avec `joblib` et expose une
    fonction `predict`.
-   `ml/views.py` : Déclare la vue Django `/predict`.
-   `config/urls.py` : Déclare la route.

------------------------------------------------------------------------

## 🚀 Lancer le serveur Django

Exécutez :

``` bash
python manage.py runserver
```

Ouvrez ensuite :\
👉 <http://127.0.0.1:8000/predict>

------------------------------------------------------------------------

## 📡 Utilisation de l'API `/predict`

La route `/predict` accepte uniquement des requêtes **POST** avec un
**JSON** au format :

``` json
{
  "inputs": [[5.1, 3.5, 1.4, 0.2]]
}
```

### Exemple avec curl

``` bash
curl -X POST http://127.0.0.1:8000/predict   -H "Content-Type: application/json"   -d '{"inputs": [[5.1, 3.5, 1.4, 0.2]]}'
```

Réponse attendue :

``` json
{"predictions": [0]}
```

------------------------------------------------------------------------

## 🧠 Fonctionnement de l'IA

-   Le modèle est un **RandomForestClassifier** de scikit-learn.
-   Il est **entraîné une seule fois** via `train_model.py` et
    sauvegardé en `.pkl`.
-   Django ne réentraîne pas le modèle à chaque requête : il le **charge
    une seule fois** en mémoire grâce à `@lru_cache` (dans
    `ml/model_store.py`).
-   Lorsqu'un utilisateur envoie une requête POST sur `/predict`, Django
    :
    1.  Récupère la liste `inputs` du JSON.
    2.  Passe ces données dans la fonction `predict`.
    3.  Retourne la prédiction du modèle sous forme de JSON.

Cela garantit que le serveur est **rapide et efficace**, sans recalcul
inutile.

------------------------------------------------------------------------

## ✅ Points importants

-   Le modèle est sauvegardé dans `models/model.pkl`.
-   Pour changer de modèle, il suffit de modifier `train_model.py`, le
    réentraîner, et relancer le serveur.
-   **Jamais** le serveur Django ne fait d'apprentissage : il ne fait
    que de l'**inférence**.

------------------------------------------------------------------------

## 🔮 Extensions possibles

-   Ajouter d'autres modèles (SVM, Réseau de neurones, etc.).
-   Ajouter une authentification pour sécuriser l'endpoint.
-   Passer sur **Django Rest Framework** pour une API plus riche.
-   Déployer sur un serveur (Heroku, AWS, etc.).
