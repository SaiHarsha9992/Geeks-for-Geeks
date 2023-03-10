//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
 
// Driver program to test above function

// } Driver Code Ends
class Solution{
  public:
    /*you are required to complete this method*/
    int convertFive(int n)
    {
        string str = to_string ( n ) ;
        for ( int i = 0 ; i < str . length( ) ; i++ )
        {
            if ( str [ i ] == '0' ) 
            str [ i ] = '5' ;
        }
        int a = stoi(str) ;
        return a ;
      }
};

//{ Driver Code Starts.
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
    	int n;
    	cin>>n;
    	Solution obj;
    	cout<<obj.convertFive(n)<<endl;
    }
}
// } Driver Code Ends