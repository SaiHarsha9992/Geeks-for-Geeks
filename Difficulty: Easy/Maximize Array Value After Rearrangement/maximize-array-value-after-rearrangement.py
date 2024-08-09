#User function Template for python3

class Solution:
    def Maximize(self, a): 
        # Complete the function
        sorted_array = sorted(a)
        mod = 10 ** 9 + 7
        sum = 0
        for i in range(len(sorted_array)):
            sum += i * sorted_array[i]

        return sum % mod



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends