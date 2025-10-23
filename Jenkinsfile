pipeline {
    agent any
    
    parameters {
        string(name: 'PAGE_TITLE', defaultValue: 'Glass Tax Calculator', description: 'Title of the HTML page')
        string(name: 'CURRENCY_SYMBOL', defaultValue: '₹', description: 'Currency symbol to use')
    }
    
    stages {
        stage('Create HTML File') {
            steps {
                script {
                    echo "Creating Glass Tax Calculator HTML file..."
                    
                    // Create the HTML content with parameter support
                    def htmlContent = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>${params.PAGE_TITLE}</title>
  <style>
    /* Reset */
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
      height: 100vh;
      background: #000;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #fff;
      overflow: hidden;
      padding: 20px;
    }

    .container {
      background: rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      padding: 40px 50px;
      width: 350px;
      box-shadow: 0 8px 32px 0 rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      transition: transform 0.3s ease;
    }

    .container:hover {
      transform: scale(1.05);
    }

    h1 {
      text-align: center;
      font-weight: 700;
      font-size: 2rem;
      margin-bottom: 10px;
      letter-spacing: 2px;
      color: #eee;
      text-shadow: 1px 1px 4px rgba(255, 255, 255, 0.2);
    }

    p {
      text-align: center;
      margin-bottom: 30px;
      font-weight: 300;
      color: #ccc;
      font-size: 0.9rem;
    }

    label {
      display: block;
      margin-bottom: 6px;
      font-weight: 600;
      font-size: 0.95rem;
      color: #bbb;
      user-select: none;
    }

    input[type="number"] {
      width: 100%;
      padding: 12px 15px;
      border-radius: 12px;
      border: none;
      outline: none;
      background: rgba(255, 255, 255, 0.15);
      color: #fff;
      font-size: 1.1rem;
      box-shadow: inset 0 0 5px rgba(255,255,255,0.4);
      transition: background 0.3s ease, box-shadow 0.3s ease;
    }

    input[type="number"]::placeholder {
      color: #fff;
      opacity: 0.7;
    }

    input[type="number"]:focus {
      background: rgba(255, 255, 255, 0.35);
      box-shadow: 0 0 8px 2px #fff;
      color: #fff;
      font-weight: 700;
    }

    .buttons {
      display: flex;
      gap: 15px;
      margin-top: 25px;
    }

    button {
      flex: 1;
      padding: 14px 0;
      border-radius: 15px;
      border: none;
      cursor: pointer;
      font-weight: 700;
      font-size: 1rem;
      background: #fff;
      color: #000;
      box-shadow: 0 5px 15px rgba(255, 255, 255, 0.5);
      transition: background 0.3s ease, transform 0.2s ease;
      user-select: none;
    }

    button:hover {
      background: #ddd;
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(220, 220, 220, 0.7);
    }

    button:active {
      transform: translateY(0);
      box-shadow: 0 4px 12px rgba(200, 200, 200, 0.4);
    }

    .results {
      margin-top: 30px;
      background: rgba(255, 255, 255, 0.12);
      padding: 20px 25px;
      border-radius: 15px;
      box-shadow: inset 0 0 10px rgba(255, 255, 255, 0.2);
      color: #eee;
    }

    .result-row {
      display: flex;
      justify-content: space-between;
      margin-bottom: 12px;
      font-size: 1.1rem;
      font-weight: 600;
      color: #eee;
      text-shadow: 1px 1px 2px rgba(255,255,255,0.2);
    }

    .result-row span.value {
      font-weight: 700;
      color: #fff;
    }

    @media (max-width: 400px) {
      .container {
        width: 90%;
        padding: 30px 25px;
      }

      button {
        font-size: 0.9rem;
        padding: 12px 0;
      }
    }
  </style>
</head>
<body>
  <div class="container" role="main" aria-label="Tax Calculator">
    <h1>${params.PAGE_TITLE}</h1>
    <p>Enter the bill amount and tax percentage to calculate the total.</p>
    
    <label for="bill">Bill Amount (${params.CURRENCY_SYMBOL})</label>
    <input type="number" id="bill" placeholder="e.g. 100" min="0" step="0.01" aria-describedby="billHelp" />

    <label for="tax">Tax Percentage (%)</label>
    <input type="number" id="tax" placeholder="e.g. 8.25" min="0" step="0.01" aria-describedby="taxHelp" />

    <div class="buttons">
      <button id="calculate" aria-label="Calculate total with tax">Calculate</button>
      <button id="reset" aria-label="Reset inputs and results">Reset</button>
    </div>

    <div class="results" aria-live="polite" aria-atomic="true">
      <div class="result-row">
        <span>Bill:</span>
        <span id="bill-result" class="value">${params.CURRENCY_SYMBOL}0.00</span>
      </div>
      <div class="result-row">
        <span>Tax Amount:</span>
        <span id="tax-result" class="value">${params.CURRENCY_SYMBOL}0.00</span>
      </div>
      <div class="result-row" style="font-size:1.3rem; color:#ccc;">
        <span>Total:</span>
        <span id="total-result" class="value">${params.CURRENCY_SYMBOL}0.00</span>
      </div>
    </div>
  </div>

  <script>
    const billInput = document.getElementById('bill');
    const taxInput = document.getElementById('tax');
    const btnCalculate = document.getElementById('calculate');
    const btnReset = document.getElementById('reset');

    const billResult = document.getElementById('bill-result');
    const taxResult = document.getElementById('tax-result');
    const totalResult = document.getElementById('total-result');

    function formatCurrency(value) {
      return '${params.CURRENCY_SYMBOL}' + value.toFixed(2);
    }

    function calculate() {
      const bill = parseFloat(billInput.value);
      const tax = parseFloat(taxInput.value);

      if (isNaN(bill) || bill < 0) {
        totalResult.textContent = "Invalid bill amount";
        return;
      }
      if (isNaN(tax) || tax < 0) {
        totalResult.textContent = "Invalid tax percentage";
        return;
      }

      const taxAmount = bill * (tax / 100);
      const total = bill + taxAmount;

      billResult.textContent = formatCurrency(bill);
      taxResult.textContent = formatCurrency(taxAmount);
      totalResult.textContent = formatCurrency(total);
    }

    function reset() {
      billInput.value = '';
      taxInput.value = '';
      billResult.textContent = '${params.CURRENCY_SYMBOL}0.00';
      taxResult.textContent = '${params.CURRENCY_SYMBOL}0.00';
      totalResult.textContent = '${params.CURRENCY_SYMBOL}0.00';
      totalResult.style.color = '#ccc';
    }

    billInput.addEventListener('input', calculate);
    taxInput.addEventListener('input', calculate);
    btnCalculate.addEventListener('click', calculate);
    btnReset.addEventListener('click', reset);
  </script>
</body>
</html>
"""
                    
                    // Write to file
                    writeFile file: 'tax-calculator.html', text: htmlContent
                    
                    // Verify file was created using Windows-compatible method
                    if (fileExists('tax-calculator.html')) {
                        def file = new File("${env.WORKSPACE}\\tax-calculator.html")
                        def fileSize = file.length()
                        echo "✅ HTML file created successfully (${fileSize} bytes)"
                    } else {
                        error("❌ Failed to create HTML file")
                    }
                }
            }
        }
        
        stage('Validate HTML') {
            steps {
                script {
                    echo "Validating HTML structure..."
                    
                    // Basic validation checks
                    def htmlContent = readFile file: 'tax-calculator.html'
                    
                    if (!htmlContent.contains('</html>')) {
                        error("HTML validation failed: Missing closing html tag")
                    }
                    
                    if (!htmlContent.contains('${params.PAGE_TITLE}')) {
                        error("HTML validation failed: Page title not found")
                    }
                    
                    echo "✅ HTML validation passed"
                }
            }
        }
        
        stage('Archive Artifact') {
            steps {
                script {
                    echo "Archiving tax-calculator.html as build artifact..."
                    archiveArtifacts artifacts: 'tax-calculator.html', fingerprint: true
                    
                    // Also create a timestamped version using Windows batch
                    def timestamp = new Date().format('yyyyMMdd-HHmmss')
                    bat "copy tax-calculator.html tax-calculator-${timestamp}.html"
                    archiveArtifacts artifacts: "tax-calculator-${timestamp}.html", fingerprint: false
                }
            }
        }
        
        stage('Generate Report') {
            steps {
                script {
                    // Create a simple build report
                    def reportContent = """
Tax Calculator Build Report
===========================
Build Number: ${env.BUILD_NUMBER}
Build URL: ${env.BUILD_URL}
Generated at: ${new Date().format('yyyy-MM-dd HH:mm:ss')}

Parameters:
- Page Title: ${params.PAGE_TITLE}
- Currency Symbol: ${params.CURRENCY_SYMBOL}

Output Files:
- tax-calculator.html (main file)
- tax-calculator-${new Date().format('yyyyMMdd-HHmmss')}.html (timestamped)

Instructions:
1. Download the HTML file from build artifacts
2. Open in any web browser
3. Use the calculator to compute tax amounts

Features:
✅ Glass morphism design
✅ Real-time calculations
✅ Responsive layout
✅ Accessibility support
"""
                    writeFile file: 'build-report.txt', text: reportContent
                    archiveArtifacts artifacts: 'build-report.txt', fingerprint: true
                }
            }
        }
    }
    
    post {
        always {
            echo "Build completed with status: ${currentBuild.result}"
        }
        success {
            echo "✅ Tax Calculator created successfully!"
            echo "📁 Download the HTML file from 'Build Artifacts' section"
        }
        failure {
            echo "❌ Failed to create Tax Calculator"
        }
        unstable {
            echo "⚠️ Build unstable - check validation results"
        }
    }
}
