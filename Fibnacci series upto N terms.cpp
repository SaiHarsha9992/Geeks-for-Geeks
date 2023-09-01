//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<long long> Series(int n) {
        // COde here
        vector<long long> v;
        v.push_back(0);
        v.push_back(1);
        for(int i = 2 ; i <=n ;i++){
            long long t = v[i-1]+v[i-2];
            v.push_back(t);
        }
        return v;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution obj;

        vector<long long> ans = obj.Series(n);
        for (auto x : ans) cout << x << " ";
        cout << "\n";
    }
    return 0;
}
// } Driver Code Ends