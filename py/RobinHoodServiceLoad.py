# https://leetcode.com/playground/Gn8SpaRJ

from collections import defaultdict, deque


# just BFS or DFS
def getLoadFactor(services: list[str], entrypoint: str):
    graph = defaultdict(list)

    for service in services:
        tokens = service.split("=")
        dependencies = tokens[1].split(",")
        for dependency in dependencies:
            if dependency != "":
                graph[tokens[0]].append(dependency)
            else:
                graph[tokens[0]] = []

    resMap = defaultdict(int)

    def dfs(root: str):
        resMap[root] += 1
        for nei in graph[root]:
            if nei in graph:
                dfs(nei)

    dfs(entrypoint)
    # q = deque([entrypoint])

    # while q:
    #     cur = q.popleft()
    #     for nei in graph[cur]:
    #         if nei in graph:
    #             q.append(nei)
    #             resMap[nei] += 1
    return [f"{node}*{resMap[node]}" for node in sorted(resMap.keys())]


service_list = [
    "logging=",
    "user=logging",
    "orders=user,foobar",
    "recommendations=user,orders",
    "dashboard=user,orders,recommendations",
]
entrypoint = "dashboard"

print(getLoadFactor(service_list, entrypoint))
