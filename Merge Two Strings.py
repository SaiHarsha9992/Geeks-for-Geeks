#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        # code here
        i,j=0,0
        l=[]
        while i<len(S1) and j<len(S2):
            l.append(S1[i])
            l.append(S2[j])
            i+=1
            j+=1
        l.append(S1[i:])
        l.append(S2[j:])
        return ''.join(l)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
# } Driver Code Ends
