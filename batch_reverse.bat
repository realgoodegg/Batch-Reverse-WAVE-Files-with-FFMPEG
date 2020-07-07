@echo off
md "%cd%\_reversedFiles"

for %%a in (*.wav) do (
    SETLOCAL enabledelayedexpansion
    for /F "delims=" %%i in ('ffprobe -v error -show_entries format_tags^=encoder -of default^=nw^=1:nk^=1 %%a 2^>^&1') do set "encoder=%%i"

    for /F "delims=" %%j in ('ffprobe -v error -show_entries stream^=codec_name -of default^=nw^=1:nk^=1 %%a 2^>^&1') do set "codec_name=%%j"

    ffmpeg -i %%a -af 'areverse' -c:a !codec_name! ".\_reversedFiles\%%~na.wav"
    bwfmetaedit ".\_reversedFiles\%%a" -a --ISFT="!encoder!"
    ENDLOCAL
)
