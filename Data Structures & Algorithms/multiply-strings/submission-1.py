class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                pos = i + j + 1
                total = product + result[pos]

                result[pos] = total % 10
                result[i + j] += total // 10

        s = "".join(map(str, result))
        return s.lstrip("0") or "0"