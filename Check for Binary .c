bool isBinary(string str)
{
    int l = str . length ( ) , c = 0 ;
    for ( int i = 0 ; i < l ; i++ ) 
	{
       if(str[i]=='0' || str[i]=='1')
       c++;
    }
    if ( c == l )
    {
    	return 1 ;
	}
	else
	{
		return 0 ;
	}
}