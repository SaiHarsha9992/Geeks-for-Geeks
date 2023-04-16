//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


class Array
{
public:
    template <class T>
    static void input(vector<T> &A,int n)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d ",&A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A)
    {
        for (int i = 0; i < A.size(); i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends
class Solution {
  public:
    long long solve(int N, vector<int> &A, vector<int> &B) {
        // code here
        sort ( A.begin(),A.end());
        sort ( B.begin(),B.end());
        
        vector<int> Ae,Ao,Be,Bo;
        long long s1 = 0 , s2 = 0 , a = 0 ;
        
        for ( int i = 0 ; i < N ; i++ )
        {
            
            s1 += A[i];
            s2 += B[i];
            
            if ( A[i]%2==0)
            {
                Ae.push_back(A[i]);
            }
            else
            {
                Ao.push_back(A[i]);
            }
            
            if ( B[i]%2==0)
            {
                Be.push_back(B[i]);
            }
            else
            {
                Bo.push_back(B[i]);
            }
        }
        
        if ( s1!=s2 || Ao.size()!=Bo.size() || Be.size()!=Ae.size() )
        {
            return -1;
        }
        
        for ( int i = 0 ; i < Ao.size() ; i++ )
        {
            a = a + abs(Ao[i]-Bo[i]);
        }
        
        for ( int i = 0 ; i < Ae.size() ; i++ )
        {
            a = a + abs(Ae[i]-Be[i]);
        }
        
        return a/4;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int N;
        scanf("%d",&N);
        
        
        vector<int> A(N);
        Array::input(A,N);
        
        
        vector<int> B(N);
        Array::input(B,N);
        
        Solution obj;
        long long res = obj.solve(N, A, B);
        
        cout<<res<<endl;
        
    }
}

// } Driver Code Ends