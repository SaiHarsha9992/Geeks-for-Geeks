//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<int> EvenOddSum(int N, int Arr[]) {
        // code here
        int e = 0 , o = 0 ;
        vector <int> v ;
        for ( int i = 0 ; i < N ; i++ )
        {
            if ( i % 2 == 0 )
            {
                e = e + Arr [ i ] ;
            }
            else 
            {
                o = o + Arr [ i ] ;
            }
        }
        v.push_back(e);
        v.push_back(o);
        return v ;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        int Arr[N];
        for (int i = 0; i < N; i++) cin >> Arr[i];
        Solution ob;
        vector<int> ans = ob.EvenOddSum(N, Arr);
        cout << ans[0] << " " << ans[1] << "\n";
    }
}
// } Driver Code Ends