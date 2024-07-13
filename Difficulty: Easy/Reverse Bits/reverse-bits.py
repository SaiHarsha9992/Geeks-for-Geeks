#User function Template for python3

class Solution:
    def reverseBits(self,n):
        #code here
        s = bin(n)
        s = s[2:]
        s = s[::-1]
        
        res = int(s, 2)
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        ob=Solution()
        print(ob.reverseBits(n))
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends