
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        freq={}
        x=y=0
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i, j in freq.items():
            if ord(i)%2==0 and j%2==0:
                x+=1
            elif ord(i)%2==1 and j%2==1:
                y+=1
        if (x+y)%2==0:
            return 'EVEN'
        return 'ODD'
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends