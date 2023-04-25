//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

public class GFG {
    public static void main(String[] args) throws Exception {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0){
            int n=sc.nextInt();
            Solution g=new Solution();
            System.out.println(g.getSmallestDivNum(n));
        }
    }
}


// } Driver Code Ends


//User function Template for Java

class Solution {
    public static long gcd ( long  a , long b )
        {
            if ( b == 0 )
            {
                return a;
            }
            return gcd(b,a%b);
        }
    public static long getSmallestDivNum(int n){
        // code here
        long r = 1 ;
        for ( long i = 2 ; i <= n ; i++ )
        {
            r = (r*i)/gcd(r,i);
        }
        return r;
    }
}
