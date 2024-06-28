//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// Function to return minimum number of jumps to end of array

class Solution{
  public:
    int minJumps(int arr[], int n){
        // Your code here
        int c = 0;
        int curr = arr[0];
        int maxReach = arr[0];
        int res = 1;
        if(n == 1){
            return 0;
        }
        if(arr[0]<=0){
            return -1;
        }
        for(int i = 1; i < n; i++){
            if(i == n-1){
                return res;
            }
            maxReach = max(maxReach, i+arr[i]);
            curr--;
            
            if(curr==0){
                res += 1;
                if(i>=maxReach){
                    return -1;
                }
                curr = maxReach-i;
            }
        }
        return -1;
    }
};


//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,j;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        Solution obj;
        cout<<obj.minJumps(arr, n)<<endl;
    }
    return 0;
}

// } Driver Code Ends