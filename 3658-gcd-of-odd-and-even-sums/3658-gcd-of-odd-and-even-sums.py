class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum=n * n
        even_sum= n*(n+1)

        def gcd(a:int,b:int):
            if b==0:
                return a
            return gcd(b,a%b)
        return gcd(odd_sum,even_sum)
        