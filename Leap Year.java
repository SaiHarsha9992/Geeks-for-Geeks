//{ Driver Code Starts
//Initial Template for Java


import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            int N = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.isLeap(N));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    static int isLeap(int N){
        //code here
         if(N%4==0 && N%100==0 && N%400!=0)
        return 0;
        
        else if(N%4!=0)
        return 0;
        
        else
        return 1;
    }
}