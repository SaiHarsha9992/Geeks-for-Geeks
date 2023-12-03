#User function Template for python3

class Solution:
    def isPrime(self,n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n%2 == 0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if n%i == 0:
                return False
        return True
    def isPali(self,n):
        s = str(n)
        if s == s[::-1]:
            return True
        else:
            return False
    def getPPS(self, a, b):
        # code here
        s = 0
        for i in range(a,b+1):
            if self.isPrime(i) and self.isPali(i):
                s += i
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(int,input().split()) 
        
        ob = Solution()
        print(ob.getPPS(a,b))
# } Driver Code Ends
