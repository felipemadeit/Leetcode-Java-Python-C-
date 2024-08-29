class Solution {

    public int lengthOfLastWord(String s) {

        String new_str = "";

        int len = 0;

        for (int i = s.length()-1; i >= 0; i--) {

           if (s.charAt(i) == ' ' && len > 0) {
                break;
           }
           else if (s.charAt(i) != ' ') {
                len ++;
           }
        }

        return len;
    }
}