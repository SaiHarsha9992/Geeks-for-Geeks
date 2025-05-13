import math
class Solution:
    def nCr(self, n, r):
        # code here
        first=math.factorial(n)
        second=math.factorial(abs(n-r))
        third=math.factorial(r)
        return(first//(second*third))


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends