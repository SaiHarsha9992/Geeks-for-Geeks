#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        # code here
        final_str = ''
        for ch in S:
            if ch.isupper():
                final_str += chr(ord('Z') + ord('A') - ord(ch))
            elif ch.islower():
                final_str += chr(ord('z') + ord('a') - ord(ch))
            else:
                final_str += ch
        return final_str


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.reciprocalString(S))
# } Driver Code Ends