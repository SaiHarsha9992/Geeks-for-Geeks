//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution{
public:
    long long fact (int n )
    {
        long long f = 1 ;
        for ( int i = 1 ; i <= n ; i++ )
        {
            f = f * i ;
        }
        return f ;
    }
    long long nPr(int n, int r){
        // code here
         long long num = fact(n);

        long long d = fact(n-r);

        

        return num/d;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, r;
        cin>>n>>r;
        
        Solution ob;
        cout<<ob.nPr(n, r)<<endl;
    }
    return 0;
}
// } Driver Code Ends