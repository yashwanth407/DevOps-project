// Test script for Tax Calculator
// This can be run in the browser console or with Node.js

console.log('🧮 Tax Calculator Test Suite');
console.log('============================');

// Test cases for the calculator logic
const testCases = [
    { bill: 100, tax: 10, expected: { taxAmount: 10, total: 110 } },
    { bill: 250, tax: 8.25, expected: { taxAmount: 20.625, total: 270.625 } },
    { bill: 1000, tax: 18, expected: { taxAmount: 180, total: 1180 } },
    { bill: 50.50, tax: 5, expected: { taxAmount: 2.525, total: 53.025 } },
    { bill: 0, tax: 10, expected: { taxAmount: 0, total: 0 } }
];

// Calculator function (same as in HTML)
function calculateTax(bill, taxPercentage) {
    if (isNaN(bill) || bill < 0) return { error: "Invalid bill amount" };
    if (isNaN(taxPercentage) || taxPercentage < 0) return { error: "Invalid tax percentage" };
    
    const taxAmount = bill * (taxPercentage / 100);
    const total = bill + taxAmount;
    
    return {
        bill: bill,
        taxAmount: taxAmount,
        total: total
    };
}

// Format currency (same as in HTML)
function formatCurrency(value) {
    return '₹' + value.toFixed(2);
}

// Run tests
let passedTests = 0;
let totalTests = testCases.length;

testCases.forEach((testCase, index) => {
    const result = calculateTax(testCase.bill, testCase.tax);
    const passed = Math.abs(result.taxAmount - testCase.expected.taxAmount) < 0.001 &&
                   Math.abs(result.total - testCase.expected.total) < 0.001;
    
    console.log(`Test ${index + 1}: ${passed ? '✅ PASS' : '❌ FAIL'}`);
    console.log(`  Input: Bill=${formatCurrency(testCase.bill)}, Tax=${testCase.tax}%`);
    console.log(`  Expected: Tax=${formatCurrency(testCase.expected.taxAmount)}, Total=${formatCurrency(testCase.expected.total)}`);
    console.log(`  Actual: Tax=${formatCurrency(result.taxAmount)}, Total=${formatCurrency(result.total)}`);
    console.log('');
    
    if (passed) passedTests++;
});

// Test edge cases
console.log('🔍 Edge Case Tests');
console.log('==================');

const edgeCases = [
    { bill: -10, tax: 5, shouldError: true },
    { bill: 100, tax: -5, shouldError: true },
    { bill: 'abc', tax: 5, shouldError: true },
    { bill: 100, tax: 'xyz', shouldError: true }
];

edgeCases.forEach((testCase, index) => {
    const result = calculateTax(testCase.bill, testCase.tax);
    const hasError = result.hasOwnProperty('error');
    const passed = testCase.shouldError === hasError;
    
    console.log(`Edge Test ${index + 1}: ${passed ? '✅ PASS' : '❌ FAIL'}`);
    console.log(`  Input: Bill=${testCase.bill}, Tax=${testCase.tax}`);
    console.log(`  Expected Error: ${testCase.shouldError}`);
    console.log(`  Has Error: ${hasError}`);
    if (hasError) console.log(`  Error: ${result.error}`);
    console.log('');
    
    if (passed) passedTests++;
    totalTests++;
});

// Summary
console.log('📊 Test Summary');
console.log('===============');
console.log(`Total Tests: ${totalTests}`);
console.log(`Passed: ${passedTests}`);
console.log(`Failed: ${totalTests - passedTests}`);
console.log(`Success Rate: ${((passedTests / totalTests) * 100).toFixed(1)}%`);

if (passedTests === totalTests) {
    console.log('🎉 All tests passed! Calculator is working correctly.');
} else {
    console.log('⚠️  Some tests failed. Please check the implementation.');
}

// Export for Node.js if available
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { calculateTax, formatCurrency, testCases };
}
