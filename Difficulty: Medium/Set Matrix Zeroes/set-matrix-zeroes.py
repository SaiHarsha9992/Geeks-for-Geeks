#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        col0,n,m=1,len(mat),len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    if j==0:
                        col0=0
                        continue 
                    else:
                        mat[i][0]=0
                        mat[0][j]=0         
        for i in range(1,n):
            if mat[i][0]==0:
                for j in range(1,m):
                    mat[i][j]=0          
        for j in range(1,m):
            if mat[0][j]==0:
                for i in range(1,n):
                    mat[i][j]=0        
        if mat[0][0]==0:
            for j in range(m):
                mat[0][j]=0       
        if col0==0:
            for i in range(n):
                mat[i][0]=0


#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends