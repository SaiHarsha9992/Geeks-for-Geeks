//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:	
	vector<int> getMoreAndLess(int arr[], int n, int x) {
	    // code here
	   vector <int> v ;
	   int c = 0 , d = 0 ;
	   for ( int i = 0 ; i < n ; i++ )
	   {
	       if ( arr [ i ] <= x ) 
	       {
	           c = c + 1 ;
	       }
	       if ( arr [ i ] >= x )
	       {
	           d = d + 1 ;
	       }
	   }
	   v . push_back ( c ) ;
	   v . push_back ( d ) ;
	   return v ;
	}
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, x;
        cin >> n >> x;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.getMoreAndLess(arr, n, x);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}

// } Driver Code Ends