#Leetcode no : Reverse Integer


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1
        if x < 0:
            x = sign * x
        else:
            sign = 1
        rem = 0
        while x > 0:
            digit = x % 10
            rem = rem*10 + digit
            x = x // 10
        if sign * rem < -2**31 or sign * rem > 2**31-1:
            return 0
        return sign * rem
        