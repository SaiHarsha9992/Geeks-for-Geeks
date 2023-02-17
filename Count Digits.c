class Solution{
public:
    int evenlyDivides(int n){
        //code here
        int r = 0 ,  c = 0 , t = n ;
        while ( t != 0 )
        {
            r = t % 10 ;
            if (  r != 0 && n % r == 0 )
            c++ ;
            t = t / 10 ;
        }
        return c ;
    }
};
