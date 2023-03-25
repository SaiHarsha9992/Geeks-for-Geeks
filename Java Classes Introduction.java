//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.Scanner;


class GFG {
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
         int l,w,h;
         l=sc.nextInt();
         w=sc.nextInt();
         h=sc.nextInt();
         task obj=new task();
         obj.set_length(l);
         obj.set_width(w);
         obj.set_height(h);
         obj.volume();
        }
    }
}


// } Driver Code Ends
//User function Template for Java

class task
{
    int length;
    int width;
    int height;
    public void set_length(int l)
    {
        //Add your code here.
        length= l;
    }
    public void set_width(int w)
    {
        //Add your code here.
        width=w;
    }
    public void set_height(int h)
    {
        //Add your code here.
        height = h ;
    }
    public void volume()
    {
        //Add your code here.
        System.out.println (length*width*height);
    }
}

//{ Driver Code Starts.

// } Driver Code Ends