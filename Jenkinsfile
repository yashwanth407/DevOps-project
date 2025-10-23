pipeline {
    agent any
    
    stages {
        stage('Create HTML File') {
            steps {
                script {
                    echo "Creating Glass Tax Calculator HTML file..."
                    
                    // Simple HTML content without parameters for testing
                    def htmlContent = """
<!DOCTYPE html>
<html>
<head>
    <title>Glass Tax Calculator</title>
    <style>
        body { 
            background: #000; 
            color: white; 
            font-family: Arial; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            margin: 0; 
        }
        .container { 
            background: rgba(255,255,255,0.1); 
            padding: 30px; 
            border-radius: 15px; 
            backdrop-filter: blur(10px); 
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Tax Calculator</h1>
        <p>Enter bill amount and tax percentage</p>
        <input type="number" id="bill" placeholder="Bill Amount">
        <input type="number" id="tax" placeholder="Tax %">
        <button onclick="calculate()">Calculate</button>
        <div id="result"></div>
    </div>
    <script>
        function calculate() {
            const bill = parseFloat(document.getElementById('bill').value);
            const tax = parseFloat(document.getElementById('tax').value);
            const taxAmount = bill * (tax / 100);
            const total = bill + taxAmount;
            document.getElementById('result').innerHTML = 'Total: ₹' + total.toFixed(2);
        }
    </script>
</body>
</html>
"""
                    
                    writeFile file: 'tax-calculator.html', text: htmlContent
                    echo "✅ HTML file created successfully"
                }
            }
        }
        
        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'tax-calculator.html', fingerprint: true
            }
        }
    }
    
    post {
        success {
            echo "✅ Tax Calculator created successfully!"
        }
        failure {
            echo "❌ Build failed"
        }
    }
}
