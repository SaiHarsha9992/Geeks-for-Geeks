//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution{
    public:
        
    // A[]: input array
    // N: size of array
    // Function to find the maximum index difference.
    int maxIndexDiff(int arr[], int n) 
    { 
        // Your code here
        if (n == 0) return 0;

    std::vector<int> leftMin(n);
    std::vector<int> rightMax(n);

    leftMin[0] = arr[0];
    for (int i = 1; i < n; ++i) {
        leftMin[i] = std::min(arr[i], leftMin[i - 1]);
    }

    // Fill rightMax array
    rightMax[n - 1] = arr[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        rightMax[i] = std::max(arr[i], rightMax[i + 1]);
    }

    // Traverse both arrays to find the maximum difference
    int i = 0, j = 0, maxDiff = 0;
    while (i < n && j < n) {
        if (leftMin[i] <= rightMax[j]) {
            maxDiff = std::max(maxDiff, j - i);
            j++;
        } else {
            i++;
        }
    }

    return maxDiff;
    }
};

//{ Driver Code Starts.
  
/* Driver program to test above functions */
int main() 
{
    int T;
    //testcases
    cin>>T;
    while(T--){
        int num;
        //size of array
        cin>>num;
        int arr[num];
        
        //inserting elements
        for (int i = 0; i<num; i++)
            cin>>arr[i];
        Solution ob;
        
        //calling maxIndexDiff() function
        cout<<ob.maxIndexDiff(arr, num)<<endl;    
        
    }
    return 0;
} 
// } Driver Code Ends