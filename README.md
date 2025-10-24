# Glass Tax Calculator - Jenkins Deployment

A beautiful, modern tax calculator with glassmorphism design that can be deployed and tested using Jenkins.

## 🚀 Quick Start

### Local Testing
1. **Using the batch script:**
   ```bash
   run_calculator.bat
   ```

2. **Manual Python server:**
   ```bash
   python -m http.server 8081
   ```

3. **Using Node.js (if available):**
   ```bash
   npm start
   ```

Then open your browser to `http://localhost:8081/index.html`

## 🔧 Jenkins Setup

### Prerequisites
- Jenkins server with pipeline support
- Python 3.x installed on Jenkins agent
- Git (if using SCM integration)

### Jenkins Pipeline Deployment

1. **Create a new Pipeline job in Jenkins:**
   - Go to Jenkins Dashboard
   - Click "New Item"
   - Enter job name (e.g., "tax-calculator-deploy")
   - Select "Pipeline"
   - Click "OK"

2. **Configure the Pipeline:**
   
   **Option A: Pipeline from SCM (Recommended)**
   - In "Pipeline" section, select "Pipeline script from SCM"
   - Choose your SCM (Git, etc.)
   - Enter repository URL
   - Set branch to build (e.g., `*/main`)
   - Script Path: `Jenkinsfile`

   **Option B: Direct Pipeline Script**
   - In "Pipeline" section, select "Pipeline script"
   - Copy and paste the contents of `Jenkinsfile` into the script area

3. **Save and Build:**
   - Click "Save"
   - Click "Build Now"

### Expected Jenkins Output

The Jenkins pipeline will:

1. ✅ **Checkout** - Verify source files
2. ✅ **Setup** - Check environment (Python/Node.js)
3. ✅ **Start Web Server** - Launch HTTP server on port 8080
4. ✅ **Test Application** - Verify server response
5. ✅ **Generate Report** - Create deployment report
6. ✅ **Display Output** - Show application status and archive artifacts

### Jenkins Artifacts

After successful build, Jenkins will archive:
- `index.html` - The main calculator application
- `app_report.txt` - Deployment report with build details
- `response.html` - Server response verification

## 📊 Application Features

- **Real-time Calculation** - Updates as you type
- **Modern UI** - Glassmorphism design with smooth animations
- **Responsive** - Works on desktop and mobile
- **Accessible** - ARIA labels and keyboard navigation
- **Currency Formatting** - Indian Rupee (₹) formatting

## 🛠️ File Structure

```
calculator/
├── index.html          # Main application file
├── Jenkinsfile         # Jenkins pipeline configuration
├── package.json        # Node.js configuration
├── run_calculator.bat  # Windows batch script for local testing
└── README.md          # This file
```

## 🔍 Troubleshooting

### Port Issues
If port 8080 is in use, the Jenkins pipeline will automatically handle this. For local testing, modify the port in:
- `run_calculator.bat`
- `package.json` scripts
- Jenkins pipeline environment variables

### Python Not Found
Ensure Python 3.x is installed and in the system PATH:
```bash
python --version
```

### Jenkins Build Fails
1. Check Jenkins console output for specific errors
2. Verify Python is available on Jenkins agent
3. Ensure proper file permissions
4. Check if ports are available

## 📈 Jenkins Pipeline Stages

| Stage | Purpose | Output |
|-------|---------|---------|
| Checkout | Verify source files exist | File validation |
| Setup | Check Python/Node.js availability | Environment info |
| Start Web Server | Launch HTTP server | Server startup logs |
| Test Application | Verify server response | HTTP response test |
| Generate Report | Create build report | Detailed deployment info |
| Display Output | Show results and archive | Final status |

## 🎯 Usage in Jenkins

1. **Build Triggers:** Set up automatic builds on code changes
2. **Notifications:** Configure email/Slack notifications for build status
3. **Deployment:** Extend pipeline to deploy to staging/production
4. **Testing:** Add automated UI tests using Selenium or Playwright

## 🌐 Accessing the Application

After Jenkins deployment:
- Local access: `http://localhost:8080/index.html`
- Jenkins workspace: Check build artifacts
- Production: Configure reverse proxy for external access

## 📝 Notes

- The application is a single-page HTML file with embedded CSS and JavaScript
- No external dependencies required for basic functionality
- Fully functional offline after initial load
- Compatible with all modern browsers

---

**Built with ❤️ for Jenkins automation and modern web development**
