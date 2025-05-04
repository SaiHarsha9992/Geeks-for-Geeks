#User function Template for python3

class Solution:
    def findSubString(self, str):
        # code here
        from collections import defaultdict
        
        n = len(set(str))
        
        left, d, ans = 0, defaultdict(int), float('inf')
        for r, e in enumerate(str):
            d[e] += 1
            while left <= r and len(d) == n:
                ans = min(ans, r-left+1)
                d[str[left]] -= 1
                if d[str[left]] == 0:
                    d.pop(str[left])
                left += 1
        return ans
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends