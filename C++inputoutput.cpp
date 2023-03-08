//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution{   
public:
    int multiplication(int A, int B){
        // code here 
        int C = A * B ;
        return C ;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int A, B;
        cin >> A >> B;
        Solution ob;
        cout << ob.multiplication(A,B) << endl;
    }
    return 0; 
} 

// } Driver Code Ends