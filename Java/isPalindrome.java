class Solution {

    public boolean isPalindrome(int x) {

        String strX = x + "";
        String reverseStringX = "";

        // Reverse for to strX
        for (int i = strX.length() -1; i >= 0; i-- ) {
            reverseStringX += strX.charAt(i);
        }

        if (strX.equals(reverseStringX)) {
            return true;
        } else {
            return false;
        }

        
    }
}