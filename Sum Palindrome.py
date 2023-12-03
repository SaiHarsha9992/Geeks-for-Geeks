#User function Template for python3

class Solution:
    def isSumPalindrome (self, n):
        # code here 
        if n == int(str(n)[::-1]):
            return n
        for i in range(5):
            n += int(str(n)[::-1])
            if n == int(str(n)[::-1]) :
                return n
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends
