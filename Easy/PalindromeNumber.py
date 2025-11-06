class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_num = str(x)
        reverse_s = str_num[::-1]

        return str_num == reverse_s