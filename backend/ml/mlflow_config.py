import mlflow

def setup_mlflow():
    mlflow.set_tracking_uri("file:../models/mlruns")
    mlflow.set_experiment("mlops_vuln_project")
