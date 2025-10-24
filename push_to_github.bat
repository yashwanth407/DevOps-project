@echo off
echo ========================================
echo Push Tax Calculator to GitHub
echo Repository: yashwanth407/DevOps-project
echo ========================================
echo.

echo Checking if git is available...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git and try again
    pause
    exit /b 1
)

echo Git is available!
echo.

echo Current directory: %CD%
echo.

echo Files to be pushed:
dir /b *.html *.md *.json Jenkinsfile *.bat 2>nul

echo.
echo ========================================
echo INSTRUCTIONS:
echo ========================================
echo.
echo 1. First, clone your repository:
echo    git clone https://github.com/yashwanth407/DevOps-project.git
echo.
echo 2. Copy these files to the cloned repository:
echo    - index.html
echo    - Jenkinsfile  
echo    - package.json
echo    - README.md
echo    - GITHUB_JENKINS_SETUP.md
echo.
echo 3. Navigate to the repository directory:
echo    cd DevOps-project
echo.
echo 4. Add, commit and push:
echo    git add .
echo    git commit -m "Add Glass Tax Calculator with Jenkins pipeline"
echo    git push origin main
echo.
echo ========================================
echo ALTERNATIVE: Auto-setup (if repo is cloned)
echo ========================================
echo.

set /p choice="Do you want to auto-copy files to DevOps-project folder? (y/n): "
if /i "%choice%"=="y" (
    if exist "DevOps-project" (
        echo Copying files to DevOps-project folder...
        copy index.html DevOps-project\ >nul
        copy Jenkinsfile DevOps-project\ >nul
        copy package.json DevOps-project\ >nul
        copy README.md DevOps-project\ >nul
        copy GITHUB_JENKINS_SETUP.md DevOps-project\ >nul
        
        echo Files copied successfully!
        echo.
        echo Now run these commands:
        echo cd DevOps-project
        echo git add .
        echo git commit -m "Add Glass Tax Calculator with Jenkins pipeline"
        echo git push origin main
    ) else (
        echo DevOps-project folder not found.
        echo Please clone the repository first:
        echo git clone https://github.com/yashwanth407/DevOps-project.git
    )
) else (
    echo Manual setup selected. Follow the instructions above.
)

echo.
echo ========================================
echo Next Steps:
echo ========================================
echo 1. Push files to GitHub (follow instructions above)
echo 2. Set up Jenkins pipeline using GITHUB_JENKINS_SETUP.md
echo 3. Run the pipeline to deploy your tax calculator
echo 4. Access the app at http://localhost:8080/index.html
echo.
pause
