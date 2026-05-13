import subprocess
from pathlib import Path

import pandas as pd

# ===== CONFIG =====
PROJECT_ROOT = Path(__file__).resolve().parents[1]
VIDEO_DIR = PROJECT_ROOT / "data" / "videos"
URLS_FILE = PROJECT_ROOT / "config" / "urls.csv"

VIDEO_DIR.mkdir(parents=True, exist_ok=True)

# ===== LOAD URLS =====
df = pd.read_csv(URLS_FILE)

for _, row in df.iterrows():
    class_name = row["class_name"]
    m3u8_url = row["m3u8_url"]

    output_path = VIDEO_DIR / f"{class_name}.mp4"

    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"Video ya descargado, se omite: {output_path.name}")
        continue

    print(f"Descargando: {class_name}")

    command = [
        "ffmpeg",
        "-i",
        m3u8_url,
        "-c",
        "copy",
        str(output_path),
    ]

    subprocess.run(command, check=True)

print("Descarga completada")
