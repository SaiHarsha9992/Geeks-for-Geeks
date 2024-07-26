#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        noOfAlpha = len(string) - string.count(' ')
    
        if noOfAlpha < 26:

            return False


        if k > 25:

            return True

 

        alphabet_map = [0] * 26

 
        for char in string:

            if char != ' ':

                alphabet_map[ord(char.lower()) - ord('a')] = 1

 

        noOfDistAlpha = alphabet_map.count(1)

 
        if noOfDistAlpha + k >= 26:
    
            return True

        else:

            return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends