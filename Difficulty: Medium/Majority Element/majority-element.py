#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        ans=-1
        count=0
        for item in arr:
            if item==ans:
                count+=1
            elif count:
                count-=1
            else:
                ans=item
                count=1
        return ans if arr.count(ans)>len(arr)//2 else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends