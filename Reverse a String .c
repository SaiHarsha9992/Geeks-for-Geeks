class Solution {
  public:
    string revStr(string S) {
        int n,i;
        char temp;
        n=S.length();
        for(int i=0;i<(n/2);i++)
        {
            temp = S[i];
            S[i] = S[n-1-i];
            S[n-1-i] = temp;
        }
        return S;
       
       
        // code here
    }
};