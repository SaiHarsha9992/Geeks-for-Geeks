//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Function to find equilibrium point in the array.
    int findEquilibrium(vector<int> &arr) {
        // code here
        map<int,int>mp;
        int sum = 0;
        for(int i=0; i<arr.size()-1; i++)
        {
            sum += arr[i];
            if(mp.find(sum) == mp.end())
            {
                mp[sum] = i+1;   
            }
        }
        
        sum = 0;
        for(int i=arr.size()-1; i>1; i--)
        {
            sum += arr[i];
            if(mp[sum] == i-1)
            {
                return mp[sum];
            }
        }
        
        return -1;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To discard any leftover newline characters
    while (t--)   // while testcases exist
    {
        vector<int> arr;
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        cout << ob.findEquilibrium(arr) << endl;
        cout << "~" << endl;
    }
}
// } Driver Code Ends