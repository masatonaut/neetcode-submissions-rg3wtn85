class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict

        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                graph[first].add(email)
                graph[email].add(first)

        visited = set()
        result = []

        def dfs(email, group):
            visited.add(email)
            group.append(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, group)

        for email in email_to_name:
            if email not in visited:
                group = []
                dfs(email, group)
                name = email_to_name[email]
                result.append([name] + sorted(group))

        return result