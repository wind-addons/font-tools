@echo off
@echo "zhTW Font Installer"

if "%~1"=="" (
    echo "Please drag and drop the font file to this batch file."
    pause
    exit /b
)

set "FONT_FILE=%~1"

if not exist "%FONT_FILE%" (
    echo "Font file not found."
    pause
    exit /b
)

copy "%FONT_FILE%" ARIALN.TTF
copy "%FONT_FILE%" FRIZQT__.TTF
copy "%FONT_FILE%" bHEI00M.TTF
copy "%FONT_FILE%" bHEI01B.TTF
copy "%FONT_FILE%" bKAI00M.TTF
copy "%FONT_FILE%" bLEI00D.TTF

@echo "All fonts copied."
pause