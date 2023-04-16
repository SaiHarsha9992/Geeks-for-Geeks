//{ Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution{
	public:
	vector<long long int> find(int l, int b, int h)
	{
	    // Code here
	    long long int L=l , B=b , H=h;
	    return { 2*(L*B + B*H + H*L) , L*B*H };
	}  
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int l, b, h;
		cin >> l >> b >> h;
		Solution ob;
		vector<long long int> ans = ob.find(l, b, h);
		for(auto i: ans)cout << i <<" ";
		cout << "\n";
	}  
	return 0;
}
// } Driver Code Ends