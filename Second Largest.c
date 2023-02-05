int print2largest(int arr[], int n ) {
int max = 0 , max1 = 0 ;
for ( int i = 0 ; i < n ; i++ )
{
	if ( max < arr [ i ] ) 
	{
		max = arr [ i ] ;
	}
}
for ( int i = 0 ; i < n ; i++ )
{
	if ( max1 < arr [ i ] && max != arr [ i ] )
	{
		max1 = arr [ i ] ;
		c++ ;
	}
}
if ( c == 0 )
{
	return -1 ;
}
else
{
	return max1 ;
}