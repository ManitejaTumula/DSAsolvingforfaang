class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        # Tree array storing [lc, rc, length, pref, suff, max_len]
        tree = [None] * (4 * n)

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            
            lc, lrc, llen, lp, ls, lb = left
            rlc, rc, rlen, rp, rs, rb = right
            
            tot_len = llen + rlen
            
            # Merge prefix
            prefix = lp
            if lrc == rlc and lp == llen:
                prefix = llen + rp
                
            # Merge suffix
            suffix = rs
            if lrc == rlc and rs == rlen:
                suffix = rlen + ls
                
            # Merge best length
            best = max(lb, rb)
            if lrc == rlc:
                best = max(best, ls + rp)
                
            return [lc, rc, tot_len, prefix, suffix, best]

        def build(node, start, end):
            if start == end:
                c = s[start]
                tree[node] = [c, c, 1, 1, 1, 1]
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, char):
            if start == end:
                tree[node] = [char, char, 1, 1, 1, 1]
                return
            
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
            
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        # Build initial segment tree
        build(1, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            # Root node (index 1) holds the global maximum at tree[1][5]
            ans.append(tree[1][5])
            
        return ans