class Solution  {
    public bool IsPalindrome(int x) {

        String strX = x.ToString();
        String strXReverse = "";

        for(int i = strX.Length-1; i >= 0; i--) {
            strXReverse += strX[i];
        }

        if (strX.Equals(strXReverse)) {
            return true;
        } else {
            return false;
        }
    }
}