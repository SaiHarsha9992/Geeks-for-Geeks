//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    string postToPre(string s) {
        // Write your code here
        int i = 0, n = s.length()-1;
        stack<string>st;
        
        while(i <= n){
            
            if((s[i]>='A'&&s[i]<='Z') || (s[i]>='a'&&s[i]<='z') || (s[i]>='0'&&s[i]<='9')){
                
                st.push(string(1,s[i]));
            }
            else{
                string t1 = st.top();
                st.pop();
                
                string t2 = st.top();
                st.pop();
                
                string co = s[i]+t2+t1;
                st.push(co);
            }
            i++;
        }
        return st.top();
    }
};

//{ Driver Code Starts.
int main() {
    int t = 1;
    cin >> t;

    // freopen ("output_gfg.txt", "w", stdout);

    while (t--) {
        // Input
        string postfix;
        cin >> postfix;

        // char marker; cin >> marker;

        Solution obj;
        cout << obj.postToPre(postfix) << endl;

        // cout << "~\n";
    }
    // fclose(stdout);

    return 0;
}

// } Driver Code Ends