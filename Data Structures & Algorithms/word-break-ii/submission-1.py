class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        result = []
        def backtrack(start, path):
            if start == len(s):
                result.append(" ".join(path))
                return
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    path.append(word)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result