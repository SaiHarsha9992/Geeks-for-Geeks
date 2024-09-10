#User function Template for python3
class Solution:
    def magicalString (ob,S):
        # code here 
        st = ''
        for i in S:
            st += chr(122-ord(i) + 97)
        return st

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.magicalString(S))
# } Driver Code Ends