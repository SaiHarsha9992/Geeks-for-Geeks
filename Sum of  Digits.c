class Solution{
public: 
    int sumOfDigits(int N){ 
	//code here
	 int s = 0 , r ; 
	 while ( N != 0 ) { 
	 r = N % 10 ; 
	 s = s + r ; 
	 N = N / 10 ; 
	 } 
	 return s ; 
	 }
};