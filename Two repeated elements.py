#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, arr , N):
        #Your code here
        my_map = {} 
        ans = [] 
        for key in arr:
            if len(ans)==2:
                break
            if key in my_map:
                my_map[key]+=1
                if my_map[key]==2:
                    ans.append(key)
            else:
                my_map[key]=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            ans = obj.twoRepeated(A,N)
            print(ans[0], ans[1])
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
