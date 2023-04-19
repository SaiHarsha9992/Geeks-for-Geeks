//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
//User function Template for C++
class Solution
{
public:
    int oppositeFaceOfDice(int N)
    {
        // Write Your Code here
        if ( N == 1 )
        {
            return 6;
        }
        else if ( N == 6 )
        {
            return 1;
        }
        else if ( N == 3 )
        {
            return 4;
        }
        else if ( N == 4 )
        {
            return 3;
        }
        else if ( N == 5 )
        {
            return 2;
        }
        else if ( N == 2 )
        {
            return 5;
        }
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        Solution ob;
        int ans  = ob.oppositeFaceOfDice(N);
        cout<<ans<<endl;
    }
    return 0;
}
// } Driver Code Ends