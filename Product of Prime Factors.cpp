//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std;

// } Driver Code Ends
class Solution{
public: 

    bool isPrime(int n){
        int a=0;
        for(int i=2; i<=n/2; i++) if(n%i==0) a=1;
        if(a==0) return 1;
        else return 0;
    }
    long long int primeProduct(int N){
        //code here
        long result=1;
       for(int i=2;i<=N;i++)
       {
           if(N%i==0)
           {
               if(isPrime(i))
               {
                   result *=i;
               }
           }
       }
       
       return result;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N;
        cin>>N;
        Solution ob;
        cout << ob.primeProduct(N) << endl;
    }
    return 0; 
}
// } Driver Code Ends