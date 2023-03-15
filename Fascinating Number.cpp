//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
public:
	
	bool fascinating(int n) {
	    // code here
	    string num = "123456789";
	    int c = 2 * n ;
	    int d = 3 * n ;
	    string e =  to_string ( n ) + to_string ( c ) + to_string ( d ) ;
	    sort ( e . begin ( ) , e . end ( ) ) ;
	    if ( e == num )
	    {
	        return true ;
	    }
	    else
	    {
	        return false ;
	    }
	    
	    
	}
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        auto ans = ob.fascinating(n);
        if (ans) {
            cout << "Fascinating\n";
        } else {
            cout << "Not Fascinating\n";
        }
    }
    return 0;
}
// } Driver Code Ends