//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while (t-- > 0) {

            String line = br.readLine();
            String[] tokens = line.split(" ");

            // Create an ArrayList to store the integers
            ArrayList<Integer> array = new ArrayList<>();

            // Parse the tokens into integers and add to the array
            for (String token : tokens) {
                array.add(Integer.parseInt(token));
            }

            int[] arr = new int[array.size()];
            int idx = 0;
            for (int i : array) arr[idx++] = i;

            Solution obj = new Solution();

            // calling maxSubarraySum() function
            System.out.println(obj.maxSubarraySum(arr));
        }
    }
}

// } Driver Code Ends

// User function Template for Java
class Solution {

    // arr: input array
    // Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(int[] arr) {
        // Initialize maxSum to the smallest possible integer value
        // Initialize currentSum to 0
        int maxSum = Integer.MIN_VALUE;
        int currentSum = 0;

        // Iterate through the array
        for (int num : arr) {
            // Add the current element to currentSum
            currentSum += num;

            // Update maxSum if currentSum is greater
            maxSum = Math.max(maxSum, currentSum);

            // Reset currentSum to 0 if it drops below 0
            if (currentSum < 0) {
                currentSum = 0;
            }
        }

        return maxSum; // Return the maximum sum found
    }
}
