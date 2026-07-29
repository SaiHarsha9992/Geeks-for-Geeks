class Solution:
    def printPat(self, n):
        #write code here
        ans = []
        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                ans.extend([j] * i)
            ans.append(-1)
        return ans