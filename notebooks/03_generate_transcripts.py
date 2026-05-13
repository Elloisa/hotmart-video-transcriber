from pathlib import Path

from faster_whisper import WhisperModel

# ===== CONFIG =====
PROJECT_ROOT = Path(__file__).resolve().parents[1]
AUDIO_DIR = PROJECT_ROOT / "data" / "audios"
TRANSCRIPT_DIR = PROJECT_ROOT / "data" / "transcripts"

TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)

# ===== FIND AUDIOS =====
audios = sorted(
    path for path in AUDIO_DIR.iterdir()
    if path.is_file() and path.suffix.lower() == ".wav"
)

pending_audios = []

for audio in audios:
    output_file = TRANSCRIPT_DIR / f"{audio.stem}.txt"

    if output_file.exists() and output_file.stat().st_size > 0:
        print(f"Transcript ya generado, se omite: {output_file.name}")
        continue

    pending_audios.append((audio, output_file))

# ===== LOAD MODEL =====
if pending_audios:
    model = WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )

    for audio, output_file in pending_audios:
        print(f"Transcribiendo: {audio.name}")

        segments, info = model.transcribe(
            str(audio),
            language="es",
            beam_size=1
        )

        with open(output_file, "w", encoding="utf-8") as f:
            for segment in segments:
                f.write(segment.text.strip() + "\n")

        print(f"Transcript guardado en: {output_file}")

else:
    print("No hay audios pendientes por transcribir.")

print("Transcripcion completada")
