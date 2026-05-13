import subprocess
from pathlib import Path

# ===== CONFIG =====
PROJECT_ROOT = Path(__file__).resolve().parents[1]
VIDEO_DIR = PROJECT_ROOT / "data" / "videos"
AUDIO_DIR = PROJECT_ROOT / "data" / "audios"
VIDEO_EXTENSIONS = {".mp4", ".m4v", ".mov", ".mkv", ".webm"}

AUDIO_DIR.mkdir(parents=True, exist_ok=True)

videos = sorted(
    path
    for path in VIDEO_DIR.iterdir()
    if path.is_file() and path.suffix.lower() in VIDEO_EXTENSIONS
)

for video in videos:
    audio_path = AUDIO_DIR / f"{video.stem}.wav"

    if audio_path.exists() and audio_path.stat().st_size > 0:
        print(f"Audio ya extraido, se omite: {audio_path.name}")
        continue

    print(f"Extrayendo audio: {video.name}")

    command = [
        "ffmpeg",
        "-i",
        str(video),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        str(audio_path),
    ]

    subprocess.run(command, check=True)

print("Extraccion de audio completada")
