string is_palindrome(int n)
{
	//Code here
	int t = n , r , s = 0 ;
	while ( n!= 0 )
	{
	r = n % 10 ;
	s = s * 10 + r ;
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