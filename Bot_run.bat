@echo off

setlocal

set REBOOT_DELAY_SECONDS=10

cd /d "%~dp0"

set TOKEN=token='6123530888:AAFDg1uB3SuaeoZY6lhH6O8-mVNjtPKAUsQ'

:loop

call %~dp0BOT_GUMRF\venv\Scripts

python BOT_GUMRF.py

echo Waiting %REBOOT_DELAY_SECONDS% seconds before next reboot...

timeout /t %REBOOT_DELAY_SECONDS% /nobreak

goto loop
