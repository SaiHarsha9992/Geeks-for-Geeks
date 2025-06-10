class Solution:
    def countStrings(self, s): 
        #code here
        n=len(s)
        freq=[0]*26
        for item in s:
            freq[ord(item)-ord("a")]+=1
        ans=(n*(n-1)//2)
        flag=False
        for val in freq:
            if val>1:
                ans-=(val*(val-1)//2)
                flag=True
        if flag:
            ans+=1
        return ans