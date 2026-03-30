class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        
        indegree = {c: 0 for c in graph}
        for c in graph:
            for next_c in graph[c]:
                indegree[next_c] += 1
        
        queue = []
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        result = []
        while queue:
            c = queue.pop(0)
            result.append(c)
            
            for next_c in graph[c]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    queue.append(next_c)

        if len(result) != len(graph):
            return ""
        
        return "".join(result)