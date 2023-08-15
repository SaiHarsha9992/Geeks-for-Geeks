//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

// Driver class
class GFG {
    
    // Driver code
	public static void main (String[] args) throws IOException{
		// Taking input using buffered reader
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int testcases = Integer.parseInt(br.readLine());
		
		// looping through all testcases
		while(testcases-- > 0){
		    int sizeOfArray = Integer.parseInt(br.readLine());
		    int arr [] = new int[sizeOfArray];
		    
		    String line = br.readLine();
		    String[] elements = line.trim().split("\\s+");
		    for(int i = 0;i<sizeOfArray;i++){
		        arr[i] =  Integer.parseInt(elements[i]);
		    }
		    
		    int sizeOfArray_M = Integer.parseInt(br.readLine());
		    int brr [] = new int[sizeOfArray_M];
		    
		    
		    line = br.readLine();
		    String[] ele = line.trim().split("\\s+");
		    for(int i = 0;i<sizeOfArray_M;i++){
		        brr[i] =  Integer.parseInt(ele[i]);
		    }
		    
		    
		    Solution obj = new Solution();
		    long res = obj.find_multiplication(arr, brr, sizeOfArray, sizeOfArray_M);
		    System.out.println(res);
		}
	}
}


            


// } Driver Code Ends


//User function Template for Java


class Solution{
    
    // Function for finding maximum and value pair
    public static long find_multiplication (int arr[], int brr[], int n, int m) {
        // Complete the Function\
          Arrays.sort(arr);
        long a=arr[n-1];
        Arrays.sort(brr);
        long b=brr[0];
        long mul=a*b;
        return mul;
    }
    
    
}

