#User function Template for python3

class Solution:
    def LastIndex(self, s, p):
        # code here
        if p not in s:
            return -1
        a=[]
        for i in range(len(s)):
            if s[i]==p:
                a.append(i)

        return a[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        p = input().strip()[0]
        
        ob=Solution()
        print(ob.LastIndex(s, p))
# } Driver Code Ends