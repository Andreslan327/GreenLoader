@echo off
setlocal

color 0a

if not exist "Audio" mkdir "Audio"
if not exist "Video" mkdir "Video"

cls
echo ***************************************
echo *            Downloader               *
echo ***************************************

set /p video_url= ^< Pega el link del video: ^>

cls
echo.
echo *********** Que quieres descargar? ***********
echo 1. Video (Mejor calidad mp4)
echo 2. Audio (MP3)
echo ***********************************************
set /p format= Escribe 1 o 2: 

if "%format%"=="2" (
    cls
    echo *************** Descargando Audio ***************
    yt-dlp.exe -x --audio-format mp3 -o "%%(title)s.%%(ext)s" %video_url%
    move /Y "*.mp3" "audio" >nul 2>&1
    move /Y "*.m4a" "audio" >nul 2>&1
    echo Audio guardado en la carpeta "Audio".
) else (
    cls
    echo *************** Descargando Video ***************
    echo Descargando mejor calidad disponible en formato MP4...
    yt-dlp.exe -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 -o "%%(title)s.%%(ext)s" %video_url%
    move /Y "*.mp4" "video" >nul 2>&1
    move /Y "*.mkv" "video" >nul 2>&1
    echo Video guardado en la carpeta "Video".
)

echo.
pause
endlocal
