#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here# Create a count dictionary for elements in A1
        count = {}
        for num in A1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    
        res = []
    
        for num in A2:
            if num in count:
                res.extend([num] * count[num])
                del count[num] 
    
        remaining_elements = sorted(count.keys())
        for num in remaining_elements:
            res.extend([num] * count[num])
    
        return res
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends