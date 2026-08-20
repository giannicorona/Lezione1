@echo off
REM Author: Gianni Corona
setlocal
cd /d "%~dp0"
set "PYTHONPATH=%~dp0src"
python -m lezione1
exit /b %ERRORLEVEL%
