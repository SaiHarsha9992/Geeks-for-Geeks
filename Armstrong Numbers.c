string armstrongNumber(int n ){
	int t = n , s = 0 , r ;
	while ( n != 0 )
	{
		r = n % 10 ;
		s = s + pow ( r , 3 ) ;
		n = n / 10 ; 
	}
	if ( s == t )
	{
		return "Yes" ;
	}
	else
	{
		return "No" ;
	}
}