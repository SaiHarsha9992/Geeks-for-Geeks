//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int findPosition(int N) {
        // code here
        int count = 0, position=1, ans = -1, i = 0;
        while(N != 0){
            if(N & 1){
                count++;
                if(i == 0) ans = position;  
                i = -1;
            }
            position++;
            N = N >> 1;
        }
        if(count == 1) return ans;
        else return -1;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;

        cin>>N;

        Solution ob;
        cout << ob.findPosition(N) << endl;
    }
    return 0;
}
// } Driver Code Ends