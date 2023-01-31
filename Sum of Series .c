class Solution{
public:
	// function to return sum of  1, 2, ... n
	long long seriesSum(int n) {
	    // code here
	    long long sum;
	    sum=(((long long) n)*((long long) n+1))/2;
	    return sum;
	}
};