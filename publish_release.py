import requests
import os
from datetime import datetime

# Configuració
repo = "tisi121/Random_C"
token = os.getenv("GITHUB_TOKEN")
tag = datetime.now().strftime("release-%Y%m%d-%H%M%S")
release_name = f"Versió {tag}"
exe_path = "./random"

# 1. Crear release
release_data = {
    "tag_name": tag,
    "name": release_name,
    "body": "Release generada automàticament per Jenkins.",
    "draft": False,
    "prerelease": False
}

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

response = requests.post(
    f"https://api.github.com/repos/{repo}/releases",
    json=release_data,
    headers=headers
)

if response.status_code != 201:
    print("❌ Error creant la release:", response.text)
    exit(1)

release = response.json()
upload_url = release["upload_url"].split("{")[0]

# 2. Pujar l'executable
with open(exe_path, "rb") as f:
    headers["Content-Type"] = "application/octet-stream"
    upload = requests.post(
        f"{upload_url}?name=random",
        headers=headers,
        data=f
    )

if upload.status_code != 201:
    print("❌ Error pujant executable:", upload.text)
    exit(1)

print("✅ Release creada i executable pujat correctament!")
