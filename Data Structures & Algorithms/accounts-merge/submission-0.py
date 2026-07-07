class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_account = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        from collections import defaultdict
        groups = defaultdict(set)
        for email, account in email_to_account.items():
            groups[uf.find(account)].add(email)
        return [[accounts[leader][0]] + sorted(emails)
            for leader, emails in groups.items()]