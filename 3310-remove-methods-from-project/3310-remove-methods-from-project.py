class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(n)]
        for u,v in invocations:
            graph[u].append(v)
        visited=set()
        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)
        dfs(k)
        for u,v in invocations:
            if u not in visited and v in visited:
                return [i for i in range(n)]
        return [i for i in range(n) if i not in visited]


        

        