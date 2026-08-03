class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber:
            columnNumber -= 1
            digit = columnNumber % 26
            result.append(chr(ord('A') + digit))
            columnNumber //= 26

        return "".join(reversed(result))