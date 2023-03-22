class Solution {
public:
    int hammingWeight(uint32_t n) {
       uint32_t b = n;
      int c = 0;
       while( b > 0 ) {
       if (b%2==1){
           c++;
       }
         b/=2;
     }
     return c;
   }
};