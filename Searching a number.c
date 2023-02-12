class Solution{
   public:
   int search(int arr[], int n, int k) { 
   // code here 
   int c = 0 ; 
   for ( int i = 0 ; i < n ; i++ ) { 
   if ( arr [ i ] == k ) {
    return i + 1 ; 
	c = 1 ; 
	}
	} 
	if ( c == 0 ) { 
	return -1 ; 
	} 
	}
	};