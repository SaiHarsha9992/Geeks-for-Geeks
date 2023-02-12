class Solution{ 
   public: 
   // Function to search x in arr 
   // arr: input array 
   // X: element to be searched for int search
   (int arr[], int N, int X) { 
   // Your code here 
   int c = 0 ; 
   for ( int i = 0 ; i < N ; i++ ) { 
   if ( arr [ i ] == X ) 
   { 
    return i ; 
	c = 1 ; }
	} 
	if ( c == 0 ) { 
	 return -1 ; 
	 } 
	 }
	 };