#User function Template for python3
from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        mp = defaultdict(list)
        def makeSort(word):
            return ''.join(sorted(list(word)))
        
        for word in arr:
            mp[makeSort(word)].append(word)
        
        res = []
        for k in mp:
            res.append(mp[k])
        
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends