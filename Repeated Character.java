//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0)
        {
            String s;
            s = sc.next();
            
            Solution ob = new Solution();
            char res = ob.firstRep(s);
            if (res == '#')
                System.out.println(-1);
            else
                System.out.println(res);
             
        }
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution
{
    char firstRep(String s)
    {
        // your code here
        for(int i =0; i<s.length()-1;i++){
            for(int j =i+1;j<s.length(); j++){
                if(s.charAt(i)==s.charAt(j))
                return s.charAt(i);
            }
        }
        return '#';
    }
}