class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # Pair each element with its original index and sort by value
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        ans = [0] * len(nums)
        
        # Group into components where adjacent sorted values differ by <= limit
        curr_vals = []
        curr_indices = []
        
        for val, idx in sorted_pairs:
            if not curr_vals or val - curr_vals[-1] <= limit:
                curr_vals.append(val)
                curr_indices.append(idx)
            else:
                # Process previous component
                curr_indices.sort()
                for i in range(len(curr_vals)):
                    ans[curr_indices[i]] = curr_vals[i]
                
                # Start new component
                curr_vals = [val]
                curr_indices = [idx]
        
        # Process the final component
        if curr_vals:
            curr_indices.sort()
            for i in range(len(curr_vals)):
                ans[curr_indices[i]] = curr_vals[i]
                
        return ans