#User function Template for python3

class stack:
    def __init__(self):
        self.s=[]
        self.minele = []
        self.top = None

    def push(self,x):
        if self.s == []:
            self.s.append(x)
            self.minele.append(x)
        else:
            self.s.append(x)
            self.minele.append(min(x , self.minele[-1]))
            
    def pop(self):
        if self.s == []:
            return -1
        else:
            ele = self.s[-1]
            self.s.pop()
            self.minele.pop()
            return ele
    def getMin(self):
        if self.minele == []:
            return -1
        else:
            return self.minele[-1]


#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        q = int(input())

        arr = [int(x) for x in input().split()]

        stk=stack()  

        qi = 0
        qn=1
        while qn <= q:
            qt = arr[qi]

            if qt == 1:
                stk.push(arr[qi+1])
                qi+=2
            elif qt==2:
                print(stk.pop(),end=' ')
                qi+=1
            else:
                print(stk.getMin(),end=' ')
                qi+=1
            qn+=1
        print()

# } Driver Code Ends