class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right=sum(weights)
        while left < right:
            mid = left + (right - left)//2
            current_weight=0
            needdays=1
            for weight in weights:
                if current_weight + weight <= mid:
                    current_weight+=weight
                else:
                    needdays+=1
                    current_weight = weight
            if needdays <= days:
                right = mid 
            else:
                left = mid+1
        return left

