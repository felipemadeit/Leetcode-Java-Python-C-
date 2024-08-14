import java.util.HashMap;
import java.util.Map;  

class Solution  {

    public int romanToInt (String s) {

        Map<Character, Integer> values = new HashMap<>();

        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);


        int finalValue = 0;
        int preValue = 0;

        for(int i = s.length()-1; i >= 0; i--) {
            int currentValue = values.get(s.charAt(i));
            if (currentValue < preValue) {
                finalValue -= currentValue;
            } else {
                finalValue += currentValue;
            }

            preValue = currentValue;
        }



        return finalValue;


    }
}