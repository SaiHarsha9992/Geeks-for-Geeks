//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int primeSum(int N){
        // code here
        int r , s = 0 ;
        while ( N != 0 )
        {
            r = N % 10 ;
            if ( r == 2 || r == 3 || r == 5 || r == 7 )
            {
                s = s + r ;
            }
            N = N / 10 ;
        }
        return s ;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        
        Solution ob;
        cout<<ob.primeSum(N)<<"\n";
    }
    return 0;
}
// } Driver Code Ends