int countofElements(int arr[],int n, int x)
{
	int c = 0 ; 
	for ( int i = 0 ; i < n ; i++ )
	{
		if ( arr [ i ] <= x )
		{
			c++ ;
		}
	}
	return c ;
}