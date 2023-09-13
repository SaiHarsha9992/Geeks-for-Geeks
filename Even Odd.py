#User function Template for python3

class Solution:
    def evenOdd(self, a, b):
        #Code here
        if a % 2 == 0:
            print(a)
            print(b)
        else:
            print(b)
            print(a)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        a, b = map(int, input().strip().split())
        obj = Solution()
        obj.evenOdd(a, b)
# } Driver Code Ends
