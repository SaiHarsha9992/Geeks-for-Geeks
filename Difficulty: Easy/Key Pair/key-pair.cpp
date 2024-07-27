//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++
class Solution {
  public:
    // Function to check if array has 2 elements
    // whose sum is equal to the given value
    bool hasArrayTwoCandidates(vector<int>& arr, int x) {
        // code here
        map<int,int> m;
        for (int i=0;i<arr.size();i++){
            int k=x-arr[i];
            if (m.find(k)!=m.end()){
                return true;
                
            }else{
                m.insert({arr[i],i});
            }
        }
        return false;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To discard any leftover newline characters
    while (t--) {
        int x;
        cin >> x;
        cin.ignore(); // To discard any leftover newline characters

        vector<int> arr;
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        auto ans = ob.hasArrayTwoCandidates(arr, x);
        cout << (ans ? "true" : "false") << endl;
    }

    return 0;
}

// } Driver Code Ends