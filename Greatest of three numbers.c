class Solution 
{ 
   public: 
   int greatestOfThree(int A, int B, int C) { 
   // code here 
   if ( A > B && A > C ) { 
   return A ; 
   } 
   else if ( B > A && B >C ) 
   { 
   return B ; 
   } 
   else { 
   return C ; 
   } 
}
};