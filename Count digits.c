int evenlyDivides(int n){
	//code here
	int count = 0 ;
	while ( n != 0 )
	{
		count++ ;
		n /= 10 ;
	}
	return count ;
}