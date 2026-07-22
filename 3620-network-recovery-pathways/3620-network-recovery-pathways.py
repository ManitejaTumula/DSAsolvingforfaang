import heapq
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n=len(online)
        g=[[] for _ in range(n)]
        l,r=float("inf"),0

        for u,v,w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v,w))
            l=min(l,w)
            r=max(r,w)

        def check(mid:int) ->bool:
            dis=[float("inf")] * n
            heap=[(0,0)]
            dis[0]=0
            while heap:
                d,u=heapq.heappop(heap)
                if d>k:
                    continue
                if u== n-1:
                    return True
                if d > dis[u]:
                    continue
                for v,w in g[u]:
                    if w >= mid:
                        new_d = d + w
                        if new_d < dis[v] and new_d <= k:
                            dis[v] = new_d
                            heapq.heappush(heap,(new_d,v))
            return False
        res=-1
        while l <= r:
            mid=(l+r)//2
            if check(mid):
                res=mid
                l=mid+1
            else:
                r=mid-1
        return res
        