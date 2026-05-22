class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            s += word1[i]
            s += word2[j]
            i += 1
            j += 1

        s += word1[i:]
        s += word2[j:]

        return s