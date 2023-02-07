class Solution{
 public:
  int product(int arr[], int n) {
   long long int p = 1 ; 
   for ( int i = 0 ; i < n ; i++ ) { 
   p = p * arr [ i ] ; 
   } 
   return p ; 
   }
   };