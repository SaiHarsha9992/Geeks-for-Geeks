class Solution {
  public:
    int mean(int n , int a[]) {
        // code here
        int s = 0 ;
        for ( int i = 0 ; i < n ; i++ )
        {
            s = s + a [ i ] ;
        }
        return s / n ;
    }
};