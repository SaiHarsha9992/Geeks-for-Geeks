class Solution{
  public:
    int count_divisors(int n){ 
	//Code here. 
	int count=0;
	 if(n%3!=0){ 
	 return 0; 
	 } 
	 for(int i=3;i<=n;i+=3){ 
	 if(n%i==0) 
	 count++; 
	 } 
	 return count;
	 }
	 };