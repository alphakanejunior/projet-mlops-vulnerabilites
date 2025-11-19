import subprocess

def scan_container(image_name):
    subprocess.run(["trivy", "image", "--format", "json", "-o", "container_report.json", image_name])

if __name__ == "__main__":
    scan_container("mlops-secure:latest")
