for %%a in ("../downloads/*.m4a") do ffmpeg -y -i "../downloads/%%~na.m4a" -acodec libmp3lame -ab 128k "../downloads/%%~na.mp3"

pause
pushd %~dp0
cd /d "..\downloads"
FOR %%b IN ("*.m4a") do DEL "%%~nb.m4a"
popd