class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1

        sign = - 1 if x < 0 else 1
        x = abs(x)

        res = 0
        while x != 0:
            digit = x % 10
            x //= 10

            if res > MAX // 10:
                return 0
            if res == MAX // 10:
                if sign == 1 and digit > MAX % 10:
                    return 0
                if sign == -1 and digit > MAX % 10 + 1:
                    return 0

            res = res * 10 + digit

        return res * sign