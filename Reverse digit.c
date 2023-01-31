long long int reverse_digit( long long int n )
{
	//code here 
	long long int r , s = 0 ;
	while ( n != 0 )
	{
		r = n % 10 ;
		s = s * 10 + r ;
		n = n / 10 ; 
	}
	return s ;
}