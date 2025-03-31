class Solution:
    def maxPartitions(self , s):
        # code here
        last_index = {ch: i for i, ch in enumerate(s)}
        ans, ind = 0, 0  

        for i, ch in enumerate(s):
            ind = max(ind, last_index[ch])
            if ind == i:
                ans += 1  

        return ans

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends