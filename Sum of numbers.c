class Solution
{
    public:
    //Function to calculate sum of all numbers present in a string.
    int findSum(string str)
    {
    	
    	// Your code here
    	int ts = 0 ;
    	for ( int i = 0 ; i < str.size( ) ; i++ )
    	{
    	    int s = 0 ;
    	    while ( str [ i ] >= 48 && str [ i ] <= 57 && i < str.size ( ))
    	    {
    	        s = s * 10 +  (str [ i ] - '0');
    	        i++ ;
    	    }
    	    ts = ts + s ;
    	}
    	return ts ;
    	
    }
};