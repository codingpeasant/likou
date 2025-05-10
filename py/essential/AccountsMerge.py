# https://leetcode.com/problems/accounts-merge/description/?envType=problem-list-v2&envId=rab78cw1
# Grind
# Neet

import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # stores doubly directed email linked to the first email of the email list
        graph = collections.defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])

        visited = set()
        # Traverse dfs of the graph to find emails that are connected to this email
        def dfs(node, connectedEmails: List[str]):
            connectedEmails.append(node)
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei, connectedEmails)

        ans = []
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in visited:
                    connectedEmails = []
                    dfs(email, connectedEmails)
                    ans.append([name] + sorted(connectedEmails))
        return ans


s = Solution()
accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
print(s.accountsMerge(accounts))
