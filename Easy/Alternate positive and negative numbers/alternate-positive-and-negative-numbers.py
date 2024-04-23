#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        arr1=[]
        arr2=[]
        arr3=[]
        for i in range(n):
            if arr[i]>=0:
                arr1.append(arr[i])
            else:
                arr2.append(arr[i])
        min_len=min(len(arr1),len(arr2))
        for i in range(min_len):
            arr3.append(arr1[i])
            arr3.append(arr2[i])
        arr3.extend(arr1[min_len:])
        arr3.extend(arr2[min_len:])
        arr[:]=arr3
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends