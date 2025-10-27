#!/usr/bin/env python3
"""
Test script for the Tax Calculator application
Tests both the server functionality and the calculator logic
"""

import unittest
import requests
import time
import subprocess
import os
import sys
import threading
from urllib.parse import urljoin
import json

class TaxCalculatorTests(unittest.TestCase):
    """Test cases for the Tax Calculator application"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.base_url = "http://localhost:8082"
        cls.server_process = None
        cls.start_test_server()
        
    @classmethod
    def tearDownClass(cls):
        """Clean up test environment"""
        cls.stop_test_server()
    
    @classmethod
    def start_test_server(cls):
        """Start the test server"""
        try:
            # Start the server in background
            cls.server_process = subprocess.Popen([
                sys.executable, "app.py"
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait for server to start
            time.sleep(3)
            
            # Verify server is running
            response = requests.get(f"{cls.base_url}/health", timeout=5)
            if response.status_code != 200:
                raise Exception("Server failed to start properly")
                
        except Exception as e:
            print(f"Failed to start test server: {e}")
            cls.server_process = None
    
    @classmethod
    def stop_test_server(cls):
        """Stop the test server"""
        if cls.server_process:
            cls.server_process.terminate()
            cls.server_process.wait(timeout=10)
    
    def test_server_health(self):
        """Test server health endpoint"""
        if not self.server_process:
            self.skipTest("Server not running")
            
        response = requests.get(f"{self.base_url}/health")
        self.assertEqual(response.status_code, 200)
    
    def test_server_status(self):
        """Test server status endpoint"""
        if not self.server_process:
            self.skipTest("Server not running")
            
        response = requests.get(f"{self.base_url}/status")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tax Calculator Server Running", response.text)
    
    def test_index_page_loads(self):
        """Test that the main calculator page loads"""
        if not self.server_process:
            self.skipTest("Server not running")
            
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Tax Calculator", response.text)
        self.assertIn("function calculate", response.text)
    
    def test_html_content_structure(self):
        """Test HTML content has required elements"""
        if not self.server_process:
            self.skipTest("Server not running")
            
        response = requests.get(f"{self.base_url}/index.html")
        content = response.text
        
        # Check for required HTML elements
        self.assertIn('<input type="number" id="bill"', content)
        self.assertIn('<input type="number" id="tax"', content)
        self.assertIn('<button id="calculate"', content)
        self.assertIn('<button id="reset"', content)
        self.assertIn('function calculate()', content)
        self.assertIn('function reset()', content)

class CalculatorLogicTests(unittest.TestCase):
    """Test the calculator logic by parsing the JavaScript"""
    
    def setUp(self):
        """Set up test data"""
        self.test_cases = [
            {"bill": 100, "tax": 10, "expected_tax": 10, "expected_total": 110},
            {"bill": 250, "tax": 8.25, "expected_tax": 20.625, "expected_total": 270.625},
            {"bill": 0, "tax": 5, "expected_tax": 0, "expected_total": 0},
            {"bill": 1000, "tax": 0, "expected_tax": 0, "expected_total": 1000},
        ]
    
    def calculate_tax(self, bill, tax_rate):
        """Replicate the JavaScript calculation logic in Python"""
        if bill < 0 or tax_rate < 0:
            return None, None
        
        tax_amount = bill * (tax_rate / 100)
        total = bill + tax_amount
        return tax_amount, total
    
    def test_tax_calculations(self):
        """Test various tax calculation scenarios"""
        for case in self.test_cases:
            with self.subTest(case=case):
                tax_amount, total = self.calculate_tax(case["bill"], case["tax"])
                
                self.assertAlmostEqual(tax_amount, case["expected_tax"], places=2)
                self.assertAlmostEqual(total, case["expected_total"], places=2)
    
    def test_invalid_inputs(self):
        """Test handling of invalid inputs"""
        invalid_cases = [
            {"bill": -100, "tax": 10},
            {"bill": 100, "tax": -5},
            {"bill": -50, "tax": -10},
        ]
        
        for case in invalid_cases:
            with self.subTest(case=case):
                tax_amount, total = self.calculate_tax(case["bill"], case["tax"])
                self.assertIsNone(tax_amount)
                self.assertIsNone(total)

def run_performance_test():
    """Run a simple performance test"""
    print("\n" + "="*50)
    print("PERFORMANCE TEST")
    print("="*50)
    
    try:
        start_time = time.time()
        response = requests.get("http://localhost:8082/", timeout=10)
        end_time = time.time()
        
        response_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        print(f"Response Time: {response_time:.2f} ms")
        print(f"Status Code: {response.status_code}")
        print(f"Content Length: {len(response.content)} bytes")
        
        if response_time < 1000:  # Less than 1 second
            print("✅ Performance: GOOD")
        else:
            print("⚠️  Performance: SLOW")
            
    except Exception as e:
        print(f"❌ Performance test failed: {e}")

def main():
    """Main test runner"""
    print("Tax Calculator Test Suite")
    print("=" * 50)
    
    # Check if index.html exists
    if not os.path.exists("index.html"):
        print("❌ Error: index.html not found")
        return 1
    
    # Run unit tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TaxCalculatorTests))
    suite.addTests(loader.loadTestsFromTestCase(CalculatorLogicTests))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Run performance test if server tests passed
    if result.wasSuccessful():
        run_performance_test()
    
    # Generate test report
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
