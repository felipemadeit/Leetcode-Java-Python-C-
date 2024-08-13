class Solution:
    def isPalindrome(self, x:int):
        """This function return a bool value, True if the int is palindrome, False if not

        Args:
            x (int): NUmber to check

        Returns:
            bool: bool depends of the number
        """
        
        str_x = str(x)
        str_x_reverse = str_x[::-1]
        
        if str_x == str_x_reverse:
            return True
        else:
            return False