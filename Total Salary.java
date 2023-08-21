import java.util.* ;
import java.io.*; 

public class Solution {
	public static int totalSalary(int basic, char ch) {
	Scanner sc = new Scanner(System.in);
        int allow;

        if (ch == 65)

        {

            allow = 1700;

            

        }

        else if(ch == 66)

        {

         allow = 1500;

        }

        else

        {

            allow = 1300;

        }

        double totalsal = ( 0.20*basic + 0.50*basic + basic + allow - 0.11*basic );

         double con = Math.round(totalsal);

         int b = (int) (con);

        return b;
	}
}
