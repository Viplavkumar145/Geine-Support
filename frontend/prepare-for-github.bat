@echo off
echo.
echo ============================================
echo   Preparing Geine-Support for GitHub Upload
echo ============================================
echo.

REM Create a clean copy for upload
if exist "GitHub-Upload" rmdir /s /q "GitHub-Upload"
mkdir "GitHub-Upload"

echo Copying files for GitHub upload...

REM Copy all files except sensitive ones
xcopy /E /I /Q "frontend" "GitHub-Upload\frontend" /EXCLUDE:exclude.txt 2>nul
xcopy /E /I /Q "backend" "GitHub-Upload\backend" /EXCLUDE:exclude.txt 2>nul

REM Remove sensitive files from the copy
if exist "GitHub-Upload\backend\.env" del "GitHub-Upload\backend\.env"
if exist "GitHub-Upload\backend\*.log" del "GitHub-Upload\backend\*.log"

REM Copy documentation files
copy "README.md" "GitHub-Upload\" 2>nul
copy "LICENSE" "GitHub-Upload\" 2>nul
copy "DEPLOYMENT.md" "GitHub-Upload\" 2>nul
copy "UPLOAD_TO_GITHUB.md" "GitHub-Upload\" 2>nul
copy ".gitignore" "GitHub-Upload\" 2>nul

echo.
echo ✅ Files prepared in 'GitHub-Upload' folder
echo.
echo What to do next:
echo 1. Go to https://github.com and create a new repository
echo 2. Upload the contents of the 'GitHub-Upload' folder
echo 3. Make sure backend/.env is NOT included (it's been excluded)
echo.
echo ⚠️  IMPORTANT: Never upload your .env file - it contains your API keys!
echo.
pause