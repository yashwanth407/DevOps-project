# GitHub + Jenkins Setup Guide
## Tax Calculator from yashwanth407/DevOps-project

This guide will help you set up Jenkins to automatically pull your tax calculator from GitHub and display the output.

## 🔧 Prerequisites

1. **Jenkins Server** with the following plugins:
   - Git Plugin
   - Pipeline Plugin
   - GitHub Integration Plugin (optional)

2. **Git** installed on Jenkins agent

3. **Python 3.x** installed on Jenkins agent

## 🚀 Step-by-Step Setup

### Step 1: Prepare Your GitHub Repository

1. **Push the calculator files to your GitHub repository:**
   ```bash
   git clone https://github.com/yashwanth407/DevOps-project.git
   cd DevOps-project
   
   # Copy the calculator files
   cp /path/to/calculator/index.html .
   cp /path/to/calculator/Jenkinsfile .
   cp /path/to/calculator/package.json .
   cp /path/to/calculator/README.md .
   
   # Commit and push
   git add .
   git commit -m "Add Glass Tax Calculator application"
   git push origin main
   ```

2. **Alternative: If repository is empty or you want to start fresh:**
   - The Jenkins pipeline will automatically create the calculator files
   - No manual setup required!

### Step 2: Create Jenkins Pipeline Job

1. **Open Jenkins Dashboard**
   - Navigate to your Jenkins server (e.g., `http://localhost:8080`)

2. **Create New Pipeline Job:**
   - Click "New Item"
   - Enter job name: `tax-calculator-github`
   - Select "Pipeline"
   - Click "OK"

3. **Configure Pipeline:**
   
   **Option A: Pipeline from SCM (Recommended)**
   - In "Pipeline" section, select "Pipeline script from SCM"
   - SCM: Git
   - Repository URL: `https://github.com/yashwanth407/DevOps-project.git`
   - Branch Specifier: `*/main`
   - Script Path: `Jenkinsfile`

   **Option B: Direct Pipeline Script**
   - In "Pipeline" section, select "Pipeline script"
   - Copy and paste the entire Jenkinsfile content

4. **Optional: Configure Build Triggers**
   - Check "GitHub hook trigger for GITScm polling" for automatic builds
   - Or set up periodic builds with "Build periodically"

5. **Save Configuration**

### Step 3: Run the Pipeline

1. **Manual Build:**
   - Click "Build Now"
   - Watch the console output

2. **Expected Pipeline Stages:**
   ```
   ✅ Checkout from GitHub
   ✅ Setup
   ✅ Start Web Server
   ✅ Test Application
   ✅ Generate Report
   ✅ Create GitHub Output Summary
   ✅ Display Output
   ```

### Step 4: Access the Output

1. **Console Output:**
   - View real-time build logs in Jenkins console
   - See GitHub deployment summary
   - View detailed deployment report

2. **Artifacts:**
   - `index.html` - The tax calculator application
   - `github_output.txt` - GitHub-specific deployment summary
   - `app_report.txt` - Detailed technical report
   - `response.html` - Server response verification

3. **Live Application:**
   - Access at: `http://localhost:8080/index.html`
   - Or the port specified in Jenkins logs

## 📊 Expected Jenkins Output

### GitHub DevOps Project Output:
```
==========================================
GITHUB DEVOPS PROJECT - TAX CALCULATOR
==========================================

Repository: yashwanth407/DevOps-project
Deployment Status: SUCCESS
Application Type: Glass Tax Calculator
Technology Stack: HTML5, CSS3, JavaScript

FEATURES:
- Real-time tax calculation
- Glassmorphism UI design
- Responsive layout
- Indian Rupee currency formatting
- Input validation and error handling

DEPLOYMENT DETAILS:
- Jenkins Pipeline: PASSED
- Web Server: Running on port 8080
- Application URL: http://localhost:8080/index.html
- Build Time: [Current Date/Time]

NEXT STEPS:
1. Access the application at the URL above
2. Test the tax calculation functionality
3. Review the glassmorphism design
4. Check responsive behavior on different screens
```

### Detailed Technical Report:
```
========================================
TAX CALCULATOR DEPLOYMENT REPORT
FROM GITHUB: yashwanth407/DevOps-project
========================================

Build Date: [Date/Time]
Application: Glass Tax Calculator
GitHub Repository: https://github.com/yashwanth407/DevOps-project.git
Branch: main
Port: 8080
Jenkins Job: [Job Name]
Build Number: [Build #]

[File listings, server status, etc.]
```

## 🔍 Troubleshooting

### Common Issues:

1. **GitHub Access Issues:**
   - Ensure repository is public or configure Jenkins credentials
   - Check repository URL is correct

2. **Port Conflicts:**
   - Pipeline will automatically handle port 8080 conflicts
   - Check Jenkins logs for actual port used

3. **Missing Dependencies:**
   - Ensure Python is installed on Jenkins agent
   - Pipeline includes fallback mechanisms

4. **Empty Repository:**
   - No problem! Pipeline will create the calculator automatically
   - Files will be generated during the build process

### Debug Steps:

1. **Check Jenkins Console Output:**
   - Look for specific error messages
   - Verify GitHub checkout success

2. **Verify Jenkins Agent:**
   ```bash
   python --version
   git --version
   ```

3. **Test Local Access:**
   - Try accessing `http://localhost:8080/index.html`
   - Check if web server is running

## 🎯 Advanced Configuration

### Webhook Setup (Optional):
1. In GitHub repository settings
2. Add webhook: `http://your-jenkins-server/github-webhook/`
3. Select "Just the push event"
4. Enable automatic builds on code changes

### Multi-Branch Pipeline:
- Use "Multibranch Pipeline" for multiple branches
- Automatically discovers branches with Jenkinsfile

### Notifications:
- Configure email notifications for build results
- Set up Slack integration for team updates

## 📝 File Structure in Repository

After successful setup, your repository should contain:
```
DevOps-project/
├── index.html          # Tax calculator application
├── Jenkinsfile         # Jenkins pipeline configuration
├── package.json        # Node.js configuration (optional)
├── README.md          # Project documentation
└── GITHUB_JENKINS_SETUP.md  # This setup guide
```

## 🌟 Success Indicators

✅ **Pipeline completes all stages successfully**
✅ **GitHub output summary displays in console**
✅ **Application accessible at localhost:8080**
✅ **Artifacts archived in Jenkins**
✅ **Tax calculator functions correctly**

---

**🎉 Congratulations! Your GitHub DevOps project with tax calculator is now running in Jenkins!**

For support or questions, check the Jenkins console logs and verify all prerequisites are met.
