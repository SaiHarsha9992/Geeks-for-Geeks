//{ Driver Code Starts


#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
	public:
		string is_AutomorphicNumber(int n)
		{
		    // Code here
		     int n1 , r , r1 ;
             n1 = pow ( n , 2 ) ;

            if(n==1 || n==0 || n==-1)

            return "Automorphic";  

            while(n)

            {

                r = n % 10 ;    
                r1 = n1 % 10 ;

                if ( r != r1 )

                return "Not Automorphic";

                n = n / 10 ;    
                n1 = n1 / 10 ;

            }

            return "Automorphic";


		}
};

//{ Driver Code Starts.
int main(){
    int T;
    cin >> T;
    while(T--)
    {
    	int n;
    	cin >> n;
    	Solution ob;
    	string ans = ob.is_AutomorphicNumber(n);
    	cout << ans <<"\n";
    }
	return 0;
}
// } Driver Code Ends