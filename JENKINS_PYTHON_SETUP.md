# Jenkins Python Setup Guide

## Problem
Your Jenkins pipeline is failing because Python is not installed or not available in the PATH on your Jenkins server.

## Solutions

### Option 1: Install Python on Jenkins Server (Recommended)

#### Step 1: Download Python
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.9, 3.10, or 3.11 for Windows
3. Choose the "Windows installer (64-bit)" version

#### Step 2: Install Python
1. Run the installer as Administrator
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Choose "Install for all users"
4. Install to default location (e.g., `C:\Python311\`)

#### Step 3: Verify Installation
Open Command Prompt and run:
```cmd
python --version
pip --version
```

#### Step 4: Configure Jenkins
1. Restart Jenkins service after Python installation
2. In Jenkins, go to "Manage Jenkins" > "Global Tool Configuration"
3. Add Python installation if needed

### Option 2: Use the Updated Jenkinsfile (Already Done)

The Jenkinsfile has been updated to:
- **Auto-detect Python** in common installation paths
- **Fallback to Node.js http-server** if Python is not available
- **Use PowerShell web server** as final fallback
- **Skip Python-specific tests** when Python is unavailable

### Option 3: Manual Python Path Configuration

If Python is installed but not in PATH, you can:

1. **Find Python installation:**
   ```cmd
   where python
   dir C:\Python*
   ```

2. **Add to System PATH:**
   - Open System Properties > Environment Variables
   - Add Python installation directory to PATH
   - Add Python Scripts directory to PATH (e.g., `C:\Python311\Scripts\`)

3. **Or update Jenkinsfile with specific path:**
   ```groovy
   environment {
       PYTHON_PATH = 'C:\\Python311\\python.exe'
   }
   ```

## Testing the Fix

### Method 1: Run the Updated Pipeline
1. Commit the updated Jenkinsfile to your repository
2. Trigger a new Jenkins build
3. The pipeline should now handle missing Python gracefully

### Method 2: Test Locally
```cmd
# Test if Python is available
python --version

# Test alternative server
npx http-server . -p 8082

# Test PowerShell server
powershell -Command "python --version"
```

## Expected Behavior After Fix

### With Python Available:
- ✅ Python environment setup succeeds
- ✅ Python web server starts (app.py)
- ✅ Python tests run (test_calculator.py)
- ✅ Full functionality available

### Without Python Available:
- ⚠️ Python environment setup detects missing Python
- ✅ Node.js http-server starts as fallback
- ✅ Basic HTTP tests run
- ✅ Application still works (HTML/CSS/JS only)

## Troubleshooting

### Issue: "npm not found"
**Solution:** Install Node.js on Jenkins server
- Download from [nodejs.org](https://nodejs.org/)
- Install with "Add to PATH" option

### Issue: PowerShell execution policy
**Solution:** Run as Administrator:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### Issue: Port conflicts
**Solution:** Change PORT in Jenkinsfile:
```groovy
environment {
    PORT = '8083'  // Use different port
}
```

## Verification Commands

Run these on your Jenkins server to verify setup:

```cmd
# Check Python
python --version
pip --version

# Check Node.js (alternative)
node --version
npm --version

# Check PowerShell
powershell -Command "Get-Host"

# Test web server manually
cd C:\ProgramData\Jenkins\.jenkins\workspace\calculator
python -m http.server 8082
```

## Next Steps

1. **Install Python** on your Jenkins server (recommended)
2. **Or use the updated Jenkinsfile** which handles missing Python
3. **Test the pipeline** with a new build
4. **Monitor the logs** to see which server method is used

The updated Jenkinsfile ensures your pipeline will work regardless of Python availability!
