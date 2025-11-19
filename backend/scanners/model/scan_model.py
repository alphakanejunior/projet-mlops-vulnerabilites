from modelscan import scan_model
import json

def scan_ml_model(model_path="model.pkl"):
    results = scan_model(model_path)
    with open("modelscan_report.json", "w") as f:
        json.dump(results, f, indent=4)

if __name__ == "__main__":
    scan_ml_model()
