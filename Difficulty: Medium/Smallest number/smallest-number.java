//{ Driver Code Starts
import java.util.*;

class GFG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();

        while (tc-- > 0) {
            int s = sc.nextInt();
            int d = sc.nextInt();

            Solution obj = new Solution();
            String res = obj.smallestNumber(s, d);

            System.out.println(res);
        }
    }
}
// } Driver Code Ends



class Solution {
    public int sumOfDigits(int n){
        int sum = 0;
        
        while (n > 0){
            sum += n % 10;
            n = n / 10;
        }
        
        return sum;
    }
    
    public String smallestNumber(int s, int d) {
        if (s > 9 * d || s < 1) {
            return "-1";
        }
        
        int initialValue = 1 * (int)Math.pow(10, d - 1);
        while (initialValue <  1 * Math.pow(10, d)) {
            if (sumOfDigits(initialValue) == s) {
                return Integer.toString(initialValue);
            }
            initialValue += 1;
        }
        
        return "-1";
    }
}
