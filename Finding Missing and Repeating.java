//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
class Solution{
public:
    vector<int> findTwoElement(vector<int> arr, int n) {
        // code here
         sort(arr.begin(),arr.end());
        vector<int>v;
        int x=0;
        for(int i=0;i<n;i++){
            if(arr[i]==arr[i+1]){
                v.push_back(arr[i]);
                x=arr[i];
                break;
            }
        }
        
        
       int sum1=0;
       int sum2=0;
       
       
       for(int i=0;i<n;i++){
           sum2=arr[i]+sum2;
           sum1=(i+1)+sum1;
       }
      
       int normal=sum2-x;
       int dif=sum1-normal;      
          v.push_back(dif);
       return v; 
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findTwoElement(a, n);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}
// } Driver Code Ends