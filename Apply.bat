@echo off
title AIJobAssistant Apply

cd /d "%~dp0"

echo.
echo ==========================================
echo        AIJobAssistant v1.5.0
echo              APPLY
echo ==========================================
echo.

python apply.py

echo.
echo ==========================================
echo Completed.
echo ==========================================
echo.

pause