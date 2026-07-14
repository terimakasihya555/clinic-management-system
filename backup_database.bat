@echo off
title Backup Clinic Database

if not exist backups (
    mkdir backups
)

set DATESTAMP=%date:~-4%%date:~3,2%%date:~0,2%
set TIMESTAMP=%time:~0,2%%time:~3,2%%time:~6,2%
set TIMESTAMP=%TIMESTAMP: =0%

echo Creating database backup...

if exist instance\clinic.sqlite (
    copy instance\clinic.sqlite backups\clinic_backup_%DATESTAMP%_%TIMESTAMP%.sqlite
    echo Backup completed successfully.
) else (
    echo Database file not found in instance\clinic.sqlite
)

pause