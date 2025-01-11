#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        t = 0
        a = ''
        for i in range(len(s)):
            if s[i] not in a:
                a += s[i]
                t = max(len(a), t)
            else:
                a = a[a.index(s[i]) + 1:] + s[i]
        return t


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends