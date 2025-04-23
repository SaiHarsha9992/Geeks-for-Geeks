#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
        res = {}
        for num in arr:
            if num not in res:
                res[num] = 1
            else:
                res[num]+=1
        result = []
        for num in res:
            if res[num]==1:
                result.append(num)
        return sorted(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends