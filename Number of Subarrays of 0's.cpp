//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

long long int no_of_subarrays(int n, vector<int> &arr) {
    // Write your code here.
    long c = 0 , p = 0 ;
    for ( int  i = 0 ; i < n ; i++ )
    {
       if ( arr [ i ] == 0 )
       {
           c++ ;
       }
       else 
       {
           p += (c * (c + 1 ) ) / 2 ;
           c = 0 ;
       }
    }
      return p + (c * (c + 1 )) / 2;
   
}

//{ Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        cout << no_of_subarrays(n, arr) << endl;
    }
}

// } Driver Code Ends