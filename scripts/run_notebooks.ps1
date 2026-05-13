. "$PSScriptRoot\..\config\paths.ps1"

function Invoke-ProjectPython {
    param(
        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    $venvPython = Join-Path $PROJECT_ROOT "venv\Scripts\python.exe"

    if (Test-Path $venvPython) {
        & $venvPython --version | Out-Null

        if ($LASTEXITCODE -eq 0) {
            & $venvPython @Arguments
        }
        else {
            Write-Warning "El Python del venv no responde. Se intentara usar Python del sistema."
            $pythonCommand = Get-Command python -ErrorAction SilentlyContinue

            if ($pythonCommand) {
                & $pythonCommand.Source @Arguments
            }
            else {
                $pyCommand = Get-Command py -ErrorAction SilentlyContinue

                if ($pyCommand) {
                    & $pyCommand.Source -3 @Arguments
                }
                else {
                    throw "No se encontro Python. Recreate el entorno virtual o instala Python."
                }
            }
        }
    }
    else {
        $pythonCommand = Get-Command python -ErrorAction SilentlyContinue

        if ($pythonCommand) {
            & $pythonCommand.Source @Arguments
        }
        else {
            $pyCommand = Get-Command py -ErrorAction SilentlyContinue

            if ($pyCommand) {
                & $pyCommand.Source -3 @Arguments
            }
            else {
                throw "No se encontro Python. Activa el entorno virtual o instala Python."
            }
        }
    }

    if ($LASTEXITCODE -ne 0) {
        throw "Error ejecutando Python con argumentos: $($Arguments -join ' ')"
    }
}

$notebookScripts = @(
    "01_download_videos.py",
    "02_extract_audio.py",
    "03_generate_transcripts.py"
)

foreach ($script in $notebookScripts) {
    $scriptPath = Join-Path $NOTEBOOK_DIR $script

    Write-Host "Ejecutando: $script"
    Invoke-ProjectPython -Arguments @($scriptPath)
}

Write-Host "Scripts ejecutados correctamente."
