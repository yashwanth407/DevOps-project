@echo off
echo Cleaning up any stuck processes...

echo Stopping PowerShell web servers...
taskkill /F /IM powershell.exe /FI "WINDOWTITLE eq Administrator*" 2>nul

echo Stopping any Python processes...
taskkill /F /IM python.exe 2>nul

echo Stopping Node.js processes...
taskkill /F /IM node.exe 2>nul

echo Checking port 8082...
netstat -ano | findstr :8082

echo Cleanup completed!
pause
