
class Solution{
 public: 
    int countCamelCase (string s) { 
	int c = 0 ; 
	for ( int i = 0 ; i < s.length ( ) ; i++ ) {
	 if ( s [ i ] >= 65 && s [ i ] <= 90 ) {
	  c++ ; 
	  } 
    } 
   return c ; 
}
};