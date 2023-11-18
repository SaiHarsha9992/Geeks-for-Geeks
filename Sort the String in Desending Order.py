#User function Template for python3
class Solution:
    def ReverseSort(self, str): 
        # code here
        s=sorted(str)
        re=s[::-1]
        z=''.join(re)
        return z


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.ReverseSort(s))
# } Driver Code Ends
