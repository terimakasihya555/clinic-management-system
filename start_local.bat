@echo off
title Clinic Management System - Local Development

echo Starting Clinic Management System in local development mode...
echo.

call venv\Scripts\activate.bat

python run.py

pause