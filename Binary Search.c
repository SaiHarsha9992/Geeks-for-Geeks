int binarysearch(int arr[] , int n , int k ) {
	//code here
	int c = 0 , index ;
	for ( int i = 0 ; i < n ; i++ )
	{
		if ( arr [ i ] == k ) 
		{
			index = i ;
			c++ ;
		}
	}
	if ( c == 0 )
	{
		return -1 ;
	}
	else
	{
		return index ;
	}
}