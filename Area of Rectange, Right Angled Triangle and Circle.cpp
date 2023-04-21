//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    vector<int> getAreas(int L , int W , int B , int H , int R) {
        // code here
        vector <int> v;
        int ar,at,ac;
        ar=L*W;
        at=0.5*B*H;
        ac=3.14*pow(R,2);
        v.push_back(ar);
        v.push_back(at);
        v.push_back(ac);
        return v;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int L,W,B,H,R;
        
        cin>>L>>W>>B>>H>>R;
        
        Solution ob;
        vector<int> ans = ob.getAreas(L,W,B,H,R);
        cout<<ans[0]<<" "<<ans[1]<<" "<<ans[2]<<endl;
    }
    return 0;
}
// } Driver Code Ends