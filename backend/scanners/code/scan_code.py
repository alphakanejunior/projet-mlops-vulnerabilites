import subprocess
import json

def scan_code():
    result = subprocess.run(["bandit", "-r", ".", "-f", "json"], capture_output=True, text=True)
    with open("bandit_report.json", "w") as f:
        f.write(result.stdout)

if __name__ == "__main__":
    scan_code()
