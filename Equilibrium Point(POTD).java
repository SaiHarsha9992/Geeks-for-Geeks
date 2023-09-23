//{ Driver Code Starts
import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        int t =
            Integer.parseInt(br.readLine().trim()); // Inputting the testcases
        while (t-- > 0) {
            
            //taking input n
            int n = Integer.parseInt(br.readLine().trim());
            long arr[] = new long[n];
            String inputLine[] = br.readLine().trim().split(" ");
            
            //adding elements to the array
            for (int i = 0; i < n; i++) {
                arr[i] = Long.parseLong(inputLine[i]);
            }

            Solution ob = new Solution();
            
            //calling equilibriumPoint() function
            System.out.println(ob.equilibriumPoint(arr, n));
        }
    }
}
// } Driver Code Ends




class Solution {

    
    // a: input array
    // n: size of array
    // Function to find equilibrium point in the array.
    public static int equilibriumPoint(long a[], int n) {

        // Your code here
         if(n==1)
        {
            return 1;
        }
        else
        {
            long b[] = new long[n];
            long c[] = new long[n];
            int k = 0 , l = 0 ; 
            long  su = 0 , p = 0 ;
            for ( int i = 0 ; i < n ; i++ )
            {
               su = su + a[i];
               b[k++] = su;
            }
            for ( int j = n-1 ; j >= 0 ; j-- )
            {
                p = p + a[j];
                c[l++] = p;
            }
            int u = 0 ; 
            int flag = 0 ;
            long d[] = new long [n];
			int m = 0;
			for ( int w = n-1 ; w >= 0 ; w-- )
			{
				d[m++]=c[w];
			}
			for ( int t = 0 ; t < n ; t++ )
            {
                    if ( b[t] == d[t])
                    {
                        u = t;
                        flag = 1;
                        break;
                    }
            }
            if ( flag == 1 )
            {
                return u+1;
            }
            else
            {
                return -1;
            }
    }
    }
    }
