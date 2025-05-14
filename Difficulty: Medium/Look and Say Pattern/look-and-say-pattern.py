class Solution:
    def countAndSay(self, n):
        # code here
        cur = "1"
        n -= 1
        while n:
            r = 0
            temp = ""
            while r < len(cur):
                flag = cur[r]
                count = 0
                while r < len(cur) and flag == cur[r]:
                    count += 1
                    r += 1
                temp += str(count) + flag
            cur = temp
            n -= 1
        return cur


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends