class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        dig_sum=0
        place_val=1
        while n > 0:
            digit=n % 10
            n=n//10
            if digit!=0:
                dig_sum+=digit
                x+=digit*place_val
                place_val*=10
        return x*dig_sum

    

        