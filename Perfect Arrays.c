 bool IsPerfect(int a[],int n)

    {

        // Complete the function

        for(int i=1;i<=n;i++)

        {

            if(a[i-1]!=a[n-i])

                return false;

        }

        return true;

    }