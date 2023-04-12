//{ Driver Code Starts
#include <bits/stdc++.h> 
using namespace std; 


// } Driver Code Ends
class Solution{
    public:
    string removeConsecutiveCharacter(string S)
    {
        // code here.
        string a = "";
        for ( int i = 0 ; i < S.length() ; i++ )
        {
            if ( i == 0 )
            {
                a += S [ i ] ;
            }
            else if ( S [ i - 1  ] != S [ i ] )
            {
                a += S [ i ] ;
            }
        }
        return a;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        Solution ob;
        cout<<ob.removeConsecutiveCharacter(s)<<endl;
    }
} 




// } Driver Code Ends