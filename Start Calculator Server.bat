@echo off
cd /d "c:\Users\yasht\OneDrive\Desktop\calculator"
echo ========================================
echo    CALCULATOR SERVER STARTING
echo ========================================
echo.
echo Server will be available at: http://localhost:8082
echo.
echo IMPORTANT: Keep this window open while using the calculator
echo Press Ctrl+C to stop the server
echo.
python -m http.server 8082
pause
