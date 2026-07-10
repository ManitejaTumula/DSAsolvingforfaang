class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        # Pair each value with its original index and sort by value
        sorted_nodes = sorted((val, i) for i, val in enumerate(nums))
        
        # Map original index to its position in the sorted array
        pos = [0] * n
        for sorted_idx, (val, orig_idx) in enumerate(sorted_nodes):
            pos[orig_idx] = sorted_idx
            
        # Binary lifting table initialization
        # LOG = 18 is enough since 2^17 = 131,072 > 10^5
        LOG = 18
        up = [[-1] * n for _ in range(LOG)]
        
        # Step 1: For each sorted node, find the furthest reachable node to its right
        right = 0
        for i in range(n):
            while right < n and sorted_nodes[right][0] - sorted_nodes[i][0] <= maxDiff:
                right += 1
            # right - 1 is the furthest index within maxDiff
            # If the furthest index is itself, it cannot make a forward jump
            if right - 1 > i:
                up[0][i] = right - 1
            else:
                up[0][i] = -1
                
        # Step 2: Build the binary lifting table
        for j in range(1, LOG):
            for i in range(n):
                if up[j-1][i] != -1:
                    up[j][i] = up[j-1][up[j-1][i]]
                else:
                    up[j][i] = -1
                    
        # Step 3: Answer queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            # Work in sorted positions
            p_u = pos[u]
            p_v = pos[v]
            
            # Ensure p_u is the smaller value position
            if p_u > p_v:
                p_u, p_v = p_v, p_u
                
            target_val = sorted_nodes[p_v][0]
            
            # Count the minimum jumps needed to reach a value >= target_val
            curr = p_u
            jumps = 0
            
            for j in range(LOG - 1, -1, -1):
                if up[j][curr] != -1 and sorted_nodes[up[j][curr]][0] < target_val:
                    curr = up[j][curr]
                    jumps += (1 << j)
                    
            # After lifting, curr is at the furthest node whose value is strictly less than target_val.
            # One final jump from here should reach or exceed target_val.
            final_jump = up[0][curr]
            if final_jump != -1 and sorted_nodes[final_jump][0] >= target_val:
                ans.append(jumps + 1)
            else:
                ans.append(-1)
                
        return ans