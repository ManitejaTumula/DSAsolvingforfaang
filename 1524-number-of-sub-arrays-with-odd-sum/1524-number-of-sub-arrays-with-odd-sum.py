class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even = 1  # Empty prefix sum is 0 (even)
        odd = 0
        prefix = 0
        count = 0
        for i in range(len(arr)):
            prefix+=arr[i]
            
            if prefix % 2 ==1:
                count+=even
                odd+=1
            else:
                count+=odd
                even+=1
        return count % MOD