class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            left, right = expand(i, i)
            if right - left + 1 > len(result):
                result = s[left:right + 1]

            left, right = expand(i, i + 1)
            if right - left + 1 > len(result):
                result = s[left:right + 1]

        return result