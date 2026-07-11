class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        component_count=0
        visited =set()
        def dfs(node):
            visited.add(node)
            nodes=1
            edges=len(graph[node])
            for nei in graph[node]:
                if nei not in visited:
                    n,e=dfs(nei)
                    nodes+=n
                    edges+=e
            return nodes,edges
        for node in range(n):
            if node not in visited:
                nodes, edges = dfs(node)
                actual_edges = edges // 2
                expected_edges = nodes * (nodes - 1) // 2
                if actual_edges == expected_edges:
                    component_count+=1
        return component_count



        

        