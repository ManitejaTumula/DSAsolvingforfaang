class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find the longest sequential prefix sum
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        # Step 2: Store elements in a set for O(1) lookups
        num_set = set(nums)
        
        # Step 3: Find the smallest missing integer >= seq_sum
        ans = seq_sum
        while ans in num_set:
            ans += 1
            
        return ans