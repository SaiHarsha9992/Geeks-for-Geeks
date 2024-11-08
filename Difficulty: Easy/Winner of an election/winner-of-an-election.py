#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        votes={}
        for i in arr:
            if i not in votes:
                votes[i]=1
            else:
                votes[i]+=1
        max_vote=0
        voter=""
        for i in votes:
            if votes[i]>max_vote:
                max_vote=votes[i]
                voter=i
            elif votes[i]==max_vote:
                voter=min(voter,i)
        return [voter,str(max_vote)]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
        print("~")
# } Driver Code Ends