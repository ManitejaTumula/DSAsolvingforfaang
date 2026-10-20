from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        return sorted(freq, key=freq.get, reverse=True)[:k]
        