//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int maxWater(vector<int> &arr) {
        // code here
        long long sum = 0;
        int n = arr.size();
        int lmax[n], rmax[n];
        lmax[0]= arr[0];
        for(int j = 1 ; j < n ; j++){
            lmax[j] = std::max(lmax[j-1], arr[j]);
        }
        rmax[n-1]=arr[n-1];
        for(int k = n-2; k >= 0; k--){
            rmax[k] = std::max(rmax[k+1], arr[k]);
        }
        for(int i = 1; i < n-1; i++){
            sum = sum + (std::min(rmax[i],lmax[i]) - arr[i]);
        }
        return sum;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;

        // Read first array
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        int res = ob.maxWater(arr);

        cout << res << endl << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends