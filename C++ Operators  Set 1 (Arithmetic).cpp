//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<int> cppOperators(int A, int B) {
        // code here
        int c , e , r , i ;
        vector <int> v ;
        c = A + B ;
        v.push_back ( c ) ;
        e = A * B ;
        v.push_back ( e ) ;
        if ( B > A )
        {
            r = B - A ;
            v.push_back ( r ) ;
            i = B / A ;
            v.push_back ( i ) ;
        }
        else 
        {
            r = A - B ;
            v.push_back ( r ) ;
            i = A / B ;
            v.push_back ( i ) ;
        }
        return v ;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int A, B;
        cin >> A >> B;
        Solution ob;
        vector<int> ans = ob.cppOperators(A, B);
        for (int u : ans) cout << u << "\n";
    }
}
// } Driver Code Ends