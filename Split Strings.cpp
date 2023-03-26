//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++

class Solution
{   
public:
    vector<string> splitString(string S) 
    { 
        // code here
        string s , sc , n ; 
        for ( int i = 0 ; i < S . size () ; i++ )
        {
            if ( S [i] >= 'A' && S [ i ] <= 'Z' || S [ i ] >= 'a' && S [ i ] <= 'z' ) 
            {
                s += S [ i ] ;
            }
            else if ( S [ i ] >= 48 && S [ i ] <= 57 )
            {
                n += S [ i ] ;
            }
            else
            {
                sc += S [ i ] ;
            }
        }
        return {s,n,sc} ;
    } 
};


//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin>>S;
        Solution ob;
        vector<string> result = ob.splitString(S);
        for (int i = 0; i < result.size(); ++i)
        {
            if(result[i] == "")
                cout<<-1<<"\n";
            else
                cout<<result[i]<<"\n";
        }
    }
    return 0; 
} 


// } Driver Code Ends