//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    void addfuc(int i, vector<int> &arr, int n){
        if (i >= n/2){
            return;
        }
        swap(arr[i], arr[n - i - 1]);
        addfuc(i+1, arr, n);
    }
    void reverseArray(vector<int> &arr) {
        // code here
        addfuc(0, arr, arr.size());    
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        ob.reverseArray(arr);
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
// } Driver Code Ends