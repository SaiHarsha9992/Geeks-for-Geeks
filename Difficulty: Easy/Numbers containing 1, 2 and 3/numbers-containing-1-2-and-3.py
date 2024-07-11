def isValid(num):
    while num!=0:
        rem=num%10
        if rem!=1 and rem!=2 and rem!=3:
            #print(num)
            return False
        num//=10
    return True

def findAll():
    #code here
    for i in range(1,1000001):
        if isValid(i)==True:
            mp[i]=1


 # Driver Code Starts
#Initial Template for Python 3

mp = {}

#Position this line where user code will be pasted.


if __name__ == '__main__':
    findAll()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr=[int(x) for x in input().strip().split()]
        arr.sort()
        flag = 0
        for i in range(n):
            if arr[i] in mp:
                print(arr[i], end=" ")
                flag=1
        if(flag==0):
            print(-1)
        else:
            print()

# } Driver Code Ends