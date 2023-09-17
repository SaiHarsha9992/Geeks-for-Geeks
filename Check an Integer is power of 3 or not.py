#User function Template for python3
class Solution:
    def isPowerof3 (ob,N):
        # code here 
        for i in range(100):
            if pow(3,i)==N:
                return "Yes"
        return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())

        ob = Solution()
        print(ob.isPowerof3(N))
# } Driver Code Ends
