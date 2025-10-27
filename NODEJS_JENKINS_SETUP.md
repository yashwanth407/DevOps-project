# Node.js Installation for Jenkins Server

## Quick Installation Steps

### 1. Download Node.js
- Go to [nodejs.org](https://nodejs.org/)
- Download "LTS" version for Windows
- Choose "Windows Installer (.msi)" 64-bit

### 2. Install Node.js
- Run installer as Administrator
- Check "Add to PATH" option
- Install for all users
- Include npm package manager

### 3. Verify Installation
```cmd
node --version
npm --version
```

### 4. Restart Jenkins
- Restart Jenkins service after installation
- This ensures Jenkins picks up the new PATH

### 5. Test in Pipeline
Your next Jenkins run should show:
```
npm install -g http-server
✅ http-server installed successfully
```

## Alternative: Use Current PowerShell Fallback
The updated Jenkinsfile will work with PowerShell web server even without Node.js!
