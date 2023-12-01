#User function Template for python3

class Solution:

    def isPossible(self, S):

        # code here
        l=len(S)
        if (l%2==0):
            if S[0:l//2]==S[l//2:]:
                return 1
            else:
                return 0
        else:
            if S[0:l//2]==S[(l//2)+1:]:
                return 1
            else:
                return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
