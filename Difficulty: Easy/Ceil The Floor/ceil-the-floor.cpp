//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User code template

class Solution {
  public:
    vector<int> getFloorAndCeil(int x, vector<int> &arr) {
        // code here
        vector<int> result;
        int n = arr.size();
        sort(arr.begin(), arr.end());
        // Find Floor
        int floor = -1;
        int low = 0, high = n - 1;
        while (low <= high)
        {
            int middle = low + (high - low) / 2;
            int element = arr[middle];
            if (element <= x)
            {
                floor = element;
                low = middle + 1;
            }
            else
                high = middle - 1;
        }
        result.push_back(floor);
        // Find Ceil
        int ceil = -1;
        low = 0, high = n - 1;
        while (low <= high)
        {
            int middle = low + (high - low) / 2;
            int element = arr[middle];
            if (element >= x)
            {
                ceil = element;
                high = middle - 1;
            }
            else
                low = middle + 1;
        }
        result.push_back(ceil);
        return result;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // Ignore the newline character after t
    while (t--) {
        vector<int> arr;
        int x;
        string input;
        cin >> x;
        cin.ignore();

        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        auto ans = ob.getFloorAndCeil(x, arr);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}
// } Driver Code Ends