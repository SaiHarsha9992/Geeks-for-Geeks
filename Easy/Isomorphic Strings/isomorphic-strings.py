#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1) != len(str2):
            return 0
        else:
            res1 = {}
            count1 = 0
            for i in str1:
                if i not in res1:
                    res1[i] = count1
                    count1 += 1
            res2 = {}
            count2 = 0
            for i in str2:
                if i not in res2:
                    res2[i] = count2
                    count2 += 1
            final1 = ""
            final2 = ""
            for i in str1:
                final1 += str(res1[i])
            for i in str2:
                final2 += str(res2[i])
            if final1 == final2:
                return 1
            else:
                return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends