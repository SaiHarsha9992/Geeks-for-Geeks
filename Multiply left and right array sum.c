int multiply(int arr[], int n)
{
    // Complete the function
    int multiply(int arr[], int n)
{
    // Complete the function
    int s = 0 , s1 = 0 ;
    for ( int i = 0 ; i < n/2 ; i++ )
    {
        s += arr [ i ] ;
    }
     for ( int i = n/2 ; i < n ; i++ )
    {
        s1 += arr [ i ] ;
    }
    int c = s * s1 ;
    return c ;
}
