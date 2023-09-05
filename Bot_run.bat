@echo off

setlocal

set REBOOT_DELAY_SECONDS=10

cd /d "%~dp0"

set TOKEN=token='Your token'

:loop

call %~dp0BOT_GUMRF\venv\Scripts

python BOT_GUMRF.py

echo Waiting %REBOOT_DELAY_SECONDS% seconds before next reboot...

timeout /t %REBOOT_DELAY_SECONDS% /nobreak

goto loop
