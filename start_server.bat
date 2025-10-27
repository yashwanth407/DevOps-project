@echo off
echo ========================================
echo TAX CALCULATOR SERVER STARTUP
echo ========================================
echo.

echo Attempting to start web server...
echo.

REM Try Python first
echo [1/3] Trying Python HTTP server on port 8082...
echo Current directory: %CD%
echo Checking for index.html...
if exist index.html (
    echo ✅ index.html found
    echo Starting Python server...
    python -m http.server 8082
) else (
    echo ❌ index.html not found in current directory
    echo Please run this script from the calculator directory
    pause
    exit /b 1
)

echo [2/3] Python not found, trying python3...
python3 -m http.server 8082 2>nul
if %errorlevel% equ 0 (
    echo ✅ Python3 server started successfully!
    echo 🌐 Access your app at: http://localhost:8082
    goto :end
)

echo [3/3] Python not available, starting PowerShell server on port 8083...
powershell -NoProfile -ExecutionPolicy Bypass -Command "& {
    Add-Type -AssemblyName System.Net.HttpListener
    if ([System.Net.HttpListener]::IsSupported) {
        Write-Host '✅ Starting PowerShell HTTP server on port 8083...' -ForegroundColor Green
        Write-Host '🌐 Access your app at: http://localhost:8083' -ForegroundColor Cyan
        Write-Host 'Press Ctrl+C to stop the server' -ForegroundColor Yellow
        Write-Host ''
        
        $listener = New-Object System.Net.HttpListener
        $listener.Prefixes.Add('http://localhost:8083/')
        $listener.Start()
        
        while ($listener.IsListening) {
            $context = $listener.GetContext()
            $response = $context.Response
            
            try {
                $content = Get-Content 'index.html' -Raw -ErrorAction Stop
                $buffer = [System.Text.Encoding]::UTF8.GetBytes($content)
                $response.ContentType = 'text/html; charset=utf-8'
                $response.ContentLength64 = $buffer.Length
                $response.OutputStream.Write($buffer, 0, $buffer.Length)
            } catch {
                $errorContent = '<h1>Error: index.html not found</h1><p>Make sure you are running this from the calculator directory.</p>'
                $buffer = [System.Text.Encoding]::UTF8.GetBytes($errorContent)
                $response.ContentType = 'text/html; charset=utf-8'
                $response.ContentLength64 = $buffer.Length
                $response.OutputStream.Write($buffer, 0, $buffer.Length)
            }
            
            $response.OutputStream.Close()
        }
    } else {
        Write-Host '❌ HTTP Listener not supported on this system' -ForegroundColor Red
    }
}"

:end
echo.
echo ========================================
echo If no server started, you can:
echo 1. Open index.html directly in your browser
echo 2. Install Python and run this script again
echo ========================================
pause
