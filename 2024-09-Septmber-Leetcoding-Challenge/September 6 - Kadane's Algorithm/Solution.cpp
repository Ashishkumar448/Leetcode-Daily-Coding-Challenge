//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

int maxSubarraySum(vector<int>& arr);

int main() {
    int t;
    cin >> t; // Inputting the testcases
    cin.ignore(); // To ignore the newline character after test cases input
    while (t-- > 0) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        vector<int> arr;
        int num;
        while (ss >> num) {
            arr.push_back(num);
        }

        // Calling maxSubarraySum function
        cout << maxSubarraySum(arr) << endl;
    }
    return 0;
}
// } Driver Code Ends

// Function to find the sum of contiguous subarray with maximum sum.
int maxSubarraySum(vector<int>& arr) {
    int maxSum = INT_MIN; // Initialize maxSum to the smallest possible integer value
    int currentSum = 0;   // Initialize currentSum to 0

    // Iterate through the array
    for (int num : arr) {
        currentSum += num;            // Add the current element to currentSum
        maxSum = max(maxSum, currentSum); // Update maxSum if currentSum is greater

        if (currentSum < 0) {  // Reset currentSum to 0 if it drops below 0
            currentSum = 0;
        }
    }

    return maxSum; // Return the maximum sum found
}
