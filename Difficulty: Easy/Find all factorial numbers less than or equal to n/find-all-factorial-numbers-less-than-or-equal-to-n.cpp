//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
   public:
  long long fact=1;
  int count=1;
  int i=0;
  vector<long long>vfact;
    vector<long long> factorialNumbers(long long n) {
        // Write Your Code here
        
        
        
        
        fact *= (count++);
        if(n+i>=fact){
            ++i;
            vfact.push_back(fact);
            
            factorialNumbers(n-1);
        }
        
        return vfact;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        long long N;
        cin >> N;
        Solution ob;
        vector<long long> ans = ob.factorialNumbers(N);
        for (auto num : ans) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends