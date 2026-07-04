class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        def dfs(node):
            for nei in graph[node]:
                if nei not in color:
                    color[nei]=1-color[node]
                    if not dfs(nei):
                        return False
                elif color[nei]==color[node]:
                    return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i]=0
            if not dfs(i):
                return False
        return True

        