@echo off
title Build Clinic Management System Desktop App

echo ============================================
echo Building Clinic Management System EXE
echo ============================================
echo.

call venv\Scripts\activate.bat

python -m pip install pyinstaller

rmdir /S /Q build 2>nul
rmdir /S /Q dist 2>nul

pyinstaller ^
  --noconfirm ^
  --clean ^
  --windowed ^
  --onedir ^
  --name "Clinic Management System" ^
  --add-data "clinic_app\templates;clinic_app\templates" ^
  --add-data "clinic_app\static;clinic_app\static" ^
  --add-data ".env.example;." ^
  desktop_launcher.py

echo.
echo ============================================
echo Build finished.
echo Output folder:
echo dist\Clinic Management System
echo ============================================
echo.

pause