#User function Template for python3

class Solution:
    def gcd(self, A, B):
        if B==0:
            return A
        return self.gcd(B, A%B)

    def lcmAndGcd(self, A , B):
        # code here 
        lst = []
        num_gcd = self.gcd(A,B)
        num_lcm = A*B//self.gcd(A, B)
        lst.append(num_lcm)
        lst.append(num_gcd)
        
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends