#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for num, count in freq.items():
            if count == 1:
                return num

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends