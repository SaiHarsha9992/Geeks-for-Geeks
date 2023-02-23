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
            int N = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.isDigitSumPalindrome(N));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    int isDigitSumPalindrome(int N) {
        // code here
          int rev=0;

        int sum=0;

        int temp = 0;

        int next = 0;

        while(N!=0){

            rev = N%10;

            sum= sum + rev;

            N/=10;

        }

    

       int num = sum;

         while(sum!=0){

            temp = sum%10;

            next = next*10 + temp;

            sum/=10;

         }

         

         if(next == num ){

             return 1;

         }else{

             return 0;

         }
    }
}