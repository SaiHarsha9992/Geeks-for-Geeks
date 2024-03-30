#User function Template for python3
from collections import Counter
class Solution:
    def firstNonRepeating(self, arr, n): 
        # Complete the function
        result = 0
        a = dict(Counter(arr))
        for i in arr:
            if a[i] == 1:
                result = i
                break
            
        return result
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends