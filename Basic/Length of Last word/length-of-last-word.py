#User function Template for python3

class Solution:

    def findLength(self, s):
        # code here
        l = s.split()
        return len(l[-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        s = input()

        solObj = Solution()

        ans = solObj.findLength(s)

        print(ans)
# } Driver Code Ends