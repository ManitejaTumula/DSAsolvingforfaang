class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original=n
        sumdigit=0
        product=1
        while n!=0:
            digit= n % 10
            sumdigit +=digit
            product *=digit
            n = n//10
        total = sumdigit + product
        return original % total==0
             