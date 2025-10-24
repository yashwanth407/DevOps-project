@echo off
echo ================================
echo Glass Tax Calculator Server
echo ================================
echo.

echo Starting web server on port 8082...
echo Open your browser and go to: http://localhost:8080/index.html
echo.
echo Press Ctrl+C to stop the server
echo.

REM Try to start with Python first
python -m http.server 8082 2>nul
if %errorlevel% neq 0 (
    echo Python not found, trying with Node.js...
    npx http-server . -p 8082 -c-1
    if %errorlevel% neq 0 (
        echo Neither Python nor Node.js found.
        echo Please install Python or Node.js to run the server.
        pause
    )
)
