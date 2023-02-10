class Solution{
  public:
  long long int find_fact(int n){ 
  // Code here. 
  long long int p = 1 ; 
  for ( int i = 1 ; i <= n ; i++ ) {
   p = p * i ; 
   } 
   return p ;
   }
   };