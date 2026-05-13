$PROJECT_ROOT = "C:\03. ML DEVELOPER\Proyectos\hotmart-video-transcriber"

$CONFIG_DIR = Join-Path $PROJECT_ROOT "config"
$DATA_DIR = Join-Path $PROJECT_ROOT "data"
$VIDEO_DIR = Join-Path $DATA_DIR "videos"
$AUDIO_DIR = Join-Path $DATA_DIR "audios"
$TRANSCRIPT_DIR = Join-Path $DATA_DIR "transcripts"
$NOTEBOOK_DIR = Join-Path $PROJECT_ROOT "notebooks"

$URLS_FILE = Join-Path $CONFIG_DIR "urls.csv"