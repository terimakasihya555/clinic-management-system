@echo off
title Seed Clinic Demo Data

echo Creating demo data for Clinic Management System...
echo.

call venv\Scripts\activate.bat

python seed_demo_data.py

echo.
echo Demo data process finished.
pause