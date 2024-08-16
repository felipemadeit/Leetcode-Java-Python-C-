using System;

class Solution {

    public string longestCommonPrefix(string[] strs) {


        if (strs == null || strs.Length == 0) {
            return "";
        }

        int minLength = strs[0].Length;

        // Encuentra la longitud mínima de todas las palabras
        foreach (var str in strs) {
            if (str.Length < minLength) {
                minLength = str.Length;
            }
        }

        string prefix = "";

        // Itera sobre cada posición hasta la longitud mínima
        for (int i = 0; i < minLength; i++) {
            char currentChar = strs[0][i];

            foreach (string s in strs) {
                if (s[i] != currentChar) {
                    return prefix;
                }
            }

            prefix += currentChar;
        }

        return prefix;
    }
}

Solution solution = new Solution();
string result = solution.longestCommonPrefix();

