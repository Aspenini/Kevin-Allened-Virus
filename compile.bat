@echo off
echo [*] Compiling the Kevin Allen Prank...

REM Make sure PyInstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [!] PyInstaller not found. Installing...
    pip install pyinstaller
)

REM Delete previous build/dist
rmdir /s /q build >nul 2>&1
rmdir /s /q dist >nul 2>&1
del kevin_apocalypse.spec >nul 2>&1

REM Compile with icon + assets
pyinstaller ^
  --noconfirm ^
  --noconsole ^
  --windowed ^
  --onefile ^
  --icon=icon.ico ^
  --add-data "kevin_allen.png;." ^
  --add-data "kevin_theme_compressed.mp3;." ^
  --add-data "kevin_supersonic_with_alarm.mp3;." ^
  kevin_apocalypse.pyw

echo [✓] Build complete! Look in the dist\ folder for KevinVirus.exe
pause
