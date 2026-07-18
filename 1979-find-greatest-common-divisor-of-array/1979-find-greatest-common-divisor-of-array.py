class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx=min(nums)
        my=max(nums)
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        return gcd(mx,my)
        