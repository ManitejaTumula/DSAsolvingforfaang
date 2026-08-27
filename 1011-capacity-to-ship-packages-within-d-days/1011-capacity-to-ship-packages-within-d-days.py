class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right= sum(weights)
        while left < right:
            mid = left + (right-left)//2
            needed_days = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight <= mid:
                    current_weight += weight
                else:
                    needed_days += 1
                    current_weight = weight
            if needed_days <= days:
                right = mid
            else:
                left = mid + 1
        return left
        
        