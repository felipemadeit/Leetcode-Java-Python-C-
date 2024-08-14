using System;
using System.Collections.Generic;

public class Solution 
{
    public int RomanToInt(string s) 
    {
        Dictionary<char, int> values = new Dictionary<char, int>
        {
            {'I', 1}, {'V', 5}, {'X', 10},
            {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
        };

        int finalValue = 0;
        int preValue = 0;

        for (int i = s.Length - 1; i >= 0; i--) 
        {
            char currentChar = s[i];
            if (!values.TryGetValue(currentChar, out int currentValue)) 
            {
                throw new ArgumentException($"Invalid Roman numeral character: {currentChar}");
            }

            if (currentValue < preValue) 
            {
                finalValue -= currentValue;
            } 
            else 
            {
                finalValue += currentValue;
            }

            preValue = currentValue;
        }

        return finalValue;
    }
}
