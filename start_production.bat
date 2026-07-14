@echo off
title Clinic Management System - Production Server

echo Starting Clinic Management System using Waitress production server...
echo.

call venv\Scripts\activate.bat

python serve.py

pause