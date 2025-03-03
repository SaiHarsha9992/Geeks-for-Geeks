from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        minq,maxq=deque(),deque()
        st,end=0,0
        ansLen=0
        ansSt,ansEnd=0,0
        for i in range(len(arr)):
            end=i
            while maxq and arr[maxq[-1]]<arr[i]:
                maxq.pop()
            maxq.append(i)
            
            while minq and arr[minq[-1]]>arr[i]:
                minq.pop()
            minq.append(i)
            
            while arr[maxq[0]]-arr[minq[0]]>x:
                st+=1
                while minq and minq[0]<st:
                    minq.popleft()
                while maxq and maxq[0]<st:
                    maxq.popleft()
            
            if end-st+1>ansLen:
                ansLen=end-st+1
                ansSt,ansEnd=st,end
                
        return arr[ansSt:ansEnd+1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends