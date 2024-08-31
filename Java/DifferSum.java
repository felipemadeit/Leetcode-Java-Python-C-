import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class DifferSum  {

    Scanner sc = new Scanner(System.in);

    public void  differSum (int n) {

        for (int i = 0; i < n; i++) {

            int x =  sc.nextInt();

            String xStr = x + "";
            int total = 0;

            for (int j= 0; j < xStr.length(); j++) {

                total += Integer.parseInt(String.valueOf(xStr.charAt(j)));
            }

            Boolean searched = true;

            Map<String, Integer> times =  new HashMap<String, Integer>();

            for (int k = 0; k < xStr.length(); k++) {

                if (times.containsKey(xStr.charAt(k))) {
                    searched = false;
                    break;
                } else {
                    times.put(String.valueOf(k), 1);
                }
            }

            System.out.println(searched);
        }
    }

    public static void main(String[] args) {
        
        DifferSum sc = new DifferSum();

        int n = 1;
        sc.differSum(n);
    }
}