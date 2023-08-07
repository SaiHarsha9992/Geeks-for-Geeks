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
            String S = read.readLine();

            Solution ob = new Solution();
            System.out.println(ob.isGoodorBad(S));
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    static boolean isVowel(char ch){
        return (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u');
    }
    static int isGoodorBad(String S) {
        // code here
        int v = 0;
    int c = 0;
    
    for(int i = 0; i < S.length(); i++){
        char ch = S.charAt(i);
        if(isVowel(ch)){
            v++;
            c = 0;
        }
        else if(ch == '?'){
            v++;
            c++;
        }
        else{
            v = 0;
            c++;
        }
        if(v > 5 || c > 3)
            return 0;
    }
    return 1;
    }
};