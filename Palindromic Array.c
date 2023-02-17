class Solution {
public:
    int PalinArray(int a[], int n)
    {
    	// code here
    	int flag = 0 ;
    	 for ( int i = 0 ; i  < n ; i++ )
        {
            int r = 0 ;
            int t = a [ i ] ;
            while ( t != 0 )
            {
               r = r * 10 + t % 10 ;
               t = t / 10 ;
            }
            if ( a [ i ] ==  r )
            {
                flag = 1 ;
            }
            else
            {
                flag = 0 ;
                break ;
            }

        }
        if ( flag == 1 )
        return 1 ;
        else
        return 0 ;
    }
};