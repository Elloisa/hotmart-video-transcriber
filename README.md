# Hotmart Video Transcriber

Flujo local para descargar videos desde URLs `.m3u8`, extraer el audio y generar transcripciones en texto con `faster-whisper`. Las transcripciones quedan listas para cargarse en herramientas como NotebookLM y facilitar el repaso del contenido.

## Estructura

```text
config/
  urls.csv                 # Lista de clases y URLs .m3u8
data/
  videos/                  # Videos descargados
  audios/                  # Audios extraidos en .wav
  transcripts/             # Transcripciones .txt
notebooks/
  01_download_videos.py
  02_extract_audio.py
  03_generate_transcripts.py
scripts/
  run_pipeline.ps1         # Ejecuta todo el flujo
  run_notebooks.ps1        # Ejecuta los scripts Python en orden
```

## Requisitos

- Windows con PowerShell.
- Python 3.9 o superior.
- `ffmpeg` instalado y disponible en el `PATH`.
- Dependencias de Python instaladas desde `requirements.txt`.

## Configuracion

El archivo `config/urls.csv` debe tener estas columnas:

```csv
class_name,m3u8_url
clase_01,https://...
clase_02,https://...
```

`class_name` se usa para nombrar los archivos generados.

## Instalacion

Desde la raiz del proyecto:

```powershell
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Si el entorno virtual ya existe pero falla al ejecutar Python, recrealo:

```powershell
Remove-Item -Recurse -Force .\venv
py -3 -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Uso

Para ejecutar todo el flujo:

```powershell
.\scripts\run_pipeline.ps1
```

El pipeline hace lo siguiente:

1. Descarga los videos listados en `config/urls.csv`.
2. Extrae audio mono a 16 kHz en formato `.wav`.
3. Genera transcripciones `.txt` con `faster-whisper`.

Los pasos son idempotentes: si un video, audio o transcript ya existe y no esta vacio, se omite.

Tambien puedes ejecutar los scripts Python en orden con:

```powershell
.\scripts\run_notebooks.ps1
```

## Salidas

Los archivos generados se guardan en:

- `data/videos/`
- `data/audios/`
- `data/transcripts/`

El contenido de `data/` no se versiona en Git porque puede incluir archivos grandes o privados.
