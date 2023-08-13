//{ Driver Code Starts
//Initial Template for Java
import java.util.*;
import java.io.*;
class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(read.readLine());
            Solution ob = new Solution();

            System.out.println(ob.nthFibonacci(n));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

//User function Template for Java
class Solution {
    static int nthFibonacci(int n){
        // code here
        if(n==1||n==2)
        return 1;
        
        int mod = (int)(Math.pow(10,9)+7);
        int a = 1 , b = 1 , c = 0;
        for(int i = 3 ; i <= n ; i++){
            c = (a+b)%mod;
            a = (b%mod);
            b = (c%mod);
        }
        return c;
    }
}