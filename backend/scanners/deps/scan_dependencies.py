import subprocess

def scan_deps():
    subprocess.run(["pip-audit", "-o", "deps_report.json", "-f", "json"])

if __name__ == "__main__":
    scan_deps()
