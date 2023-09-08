//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            
            int n = Integer.parseInt(read.readLine().trim());
            
            String input[] = read.readLine().trim().split(" ");
            
            char arr[] = new char[n];
            for(int i = 0; i < n; i++){
                arr[i] = input[i].charAt(0);
            }
            
            
            Solution ob = new Solution();
            String ans = ob.chartostr(arr, n);
            
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution{
    public String chartostr(char arr[], int N){
        String s = new String(arr);
        return s;
    }
}