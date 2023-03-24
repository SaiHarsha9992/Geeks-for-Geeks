//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
	public:
		long long int sum_of_square_oddNumbers(long long int n)
		{
		    // Code here.
		    long long int s = 0 ;
		    for ( int i = 1 ; i <= n ; i++)
		    {
		        s = s + pow(2*i-1,2);
		    }
		    return s ;
		}
};

//{ Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
    	long long int n;
    	cin >> n;
    	Solution ob;
    	long long int  ans = ob.sum_of_square_oddNumbers(n);
    	cout << ans <<"\n";
    }
	return 0;
}
// } Driver Code Ends