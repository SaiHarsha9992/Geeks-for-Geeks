//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main(String[] args) throws IOException
	{
	        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while(t-->0)
        {
            long n = Long.parseLong(br.readLine().trim());
            long a[] = new long[(int)(n)];
            String inputLine[] = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                a[i] = Long.parseLong(inputLine[i]);
            }
            
            Compute obj = new Compute();
            long[] product = obj.minAnd2ndMin(a, n); 
            if(product[0]==-1)
                System.out.println(product[0]);
            else
                System.out.println(product[0]+" "+product[1]);
            
        }
	}
}


// } Driver Code Ends


//User function Template for Java


class Compute 
{
    public long[] minAnd2ndMin(long a[], long n)  
    {
          Arrays.sort(a);
        long arr[]=new long[2];
         if(n==1){
           arr[0]=-1;
           arr[1]=-1;
        }
        else{
        arr[0]=a[0];
        for(int i=1;i<n;i++){
            
            if(a[i]>arr[0]){
            arr[1]=a[i];
            break;
            }
            else if(a[0]==a[(int)n-1]){
                arr[0]=-1;
                arr[1]=-1;
            }
            
        }
        }
        return arr;
    }
}
