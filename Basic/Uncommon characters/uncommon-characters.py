#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        s=''
        b=''
        for i in A:
            if i not in B:
                s+=i
        for i in B:
            if i not in A:
                b+=i
        if not s and not b:
            return -1
        return ''.join(sorted(set(s+b)))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends