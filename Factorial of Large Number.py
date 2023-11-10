#User function Template for python3
import math
class Solution:
    def factorial(self, N):
        #code here
        fact = 1
        ans =[]
        if N == 0:
            ans.append(N)
            return ans
        while N != 0:
            fact = fact * N
            N = N-1
        st = str(fact)
        for i in st:
            ans.append(int(i))
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends
