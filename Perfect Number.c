class Solution {
  public:
  int fact ( int x )
  {
      int f = 1 ;
      for ( int i = 1 ; i <= x ; i++ )
      {
          f = f * i ;
      }
      return f ;
      
  }
    int isPerfect(int n) {
        // code here
        int r , s = 0 , t = n ;
        while ( n != 0 )
        {
            r = n % 10 ;
            s = s + fact ( r ) ;
            n = n / 10 ;
        }
        if ( t == s )
        {
            return 1 ;
        }
        else
        {
            return 0 ;
        }
    }
};
