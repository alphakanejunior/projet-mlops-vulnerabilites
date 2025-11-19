import json

def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return {}

def unify_reports():
    final = {
        "code": load_json("bandit_report.json"),
        "dependencies": load_json("deps_report.json"),
        "model": load_json("modelscan_report.json"),
        "container": load_json("container_report.json")
    }

    with open("unified_report.json", "w") as f:
        json.dump(final, f, indent=4)

if __name__ == "__main__":
    unify_reports()
