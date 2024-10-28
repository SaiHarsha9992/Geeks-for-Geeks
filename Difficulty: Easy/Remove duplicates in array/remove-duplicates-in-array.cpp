//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    vector<int> removeDuplicate(vector<int>& arr) {
        // code here
        int n = arr.size();
        vector<int> res;
        vector<int> freq(101, -1);
        for(int i = 0; i < n; i++){
            if(freq[arr[i]] == -1){
                freq[arr[i]] = i;
            }
            else{
                arr[i] = 0;
            }
        }
        
        for(int i = 0; i < n; i++){
            if(arr[i] != 0){
                res.push_back(arr[i]);
            }
        }
        
        return res;
    }
};

//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        vector<int> ans = obj.removeDuplicate(arr);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends