#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        n = len(nums)
        res = [1] * n  

        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n-1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends