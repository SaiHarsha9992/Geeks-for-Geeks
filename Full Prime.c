class Solution{
    public:
    bool Isprime(int &n){
        if(n<=1) return false;
        if(n==2) return true;
        for(int i=2; i*i<=n; i++){
            if(n%i==0) return false;
        }
        return true;
        
    }
	int fullPrime(int N){
	  if(!Isprime(N)) return 0;
	   while(N!=0){
	       int ans = N%10;
	     if(!Isprime( ans)){
	       return 0;
	     }
	     N = N/10;
	   }
	   
	   return 1;
	    //code here
	}
};