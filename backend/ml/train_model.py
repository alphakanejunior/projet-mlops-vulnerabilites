import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import pickle

from mlflow_config import setup_mlflow

def train_model():
    setup_mlflow()

    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.3, random_state=42
    )

    n_estimators = 100
    max_depth = 5

    with mlflow.start_run():

        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth
        )
        model.fit(X_train, y_train)

        accuracy = model.score(X_test, y_test)

        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(model, "model")

        with open("model.pkl", "wb") as f:
            pickle.dump(model, f)

        print("Model enregistré + exporté en model.pkl")

if __name__ == "__main__":
    train_model()
