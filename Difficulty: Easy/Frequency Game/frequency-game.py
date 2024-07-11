#User function Template for python3


def LargButMinFreq(arr,n):
    #code here
    d = {}
    
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    min_freq = float('inf')
    for freq in d.values():
        if freq < min_freq:
            min_freq = freq

    max_element = -float('inf')
    for key, value in d.items():
        if value == min_freq and key > max_element:
            max_element = key
    
    return max_element


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends