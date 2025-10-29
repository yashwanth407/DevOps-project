@echo off
echo Starting Calculator Web Server...
echo.

REM Try Python 3 first
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Found Python! Starting server on http://localhost:8082
    echo Press Ctrl+C to stop the server
    echo.
    python -m http.server 8082
    goto :end
)

REM Try Python command
python3 --version >nul 2>&1
if %errorlevel% == 0 (
    echo Found Python3! Starting server on http://localhost:8082
    echo Press Ctrl+C to stop the server
    echo.
    python3 -m http.server 8082
    goto :end
)

REM Fallback to PowerShell HTTP server
echo Python not found. Trying PowerShell server...
echo Starting server on http://localhost:8082
echo Press Ctrl+C to stop the server
echo.
powershell -Command "& {
    try {
        $listener = New-Object System.Net.HttpListener
        $listener.Prefixes.Add('http://localhost:8082/')
        $listener.Start()
        Write-Host 'Server running at http://localhost:8082'
        Write-Host 'Press Ctrl+C to stop'
        
        while ($listener.IsListening) {
            $context = $listener.GetContext()
            $request = $context.Request
            $response = $context.Response
            
            if ($request.Url.AbsolutePath -eq '/' -or $request.Url.AbsolutePath -eq '/index.html') {
                $content = Get-Content 'index.html' -Raw -Encoding UTF8
                $buffer = [System.Text.Encoding]::UTF8.GetBytes($content)
                $response.ContentType = 'text/html; charset=utf-8'
                $response.ContentLength64 = $buffer.Length
                $response.OutputStream.Write($buffer, 0, $buffer.Length)
            }
            $response.Close()
        }
    } catch {
        Write-Host 'PowerShell server failed. Please open index.html directly in your browser.'
        Read-Host 'Press Enter to exit'
    }
}"

:end
if %errorlevel% neq 0 (
    echo.
    echo All server options failed!
    echo Please open index.html directly in your browser.
    echo File location: %~dp0index.html
    pause
)
