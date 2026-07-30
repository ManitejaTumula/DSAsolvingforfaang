class Solution:
    def minimumPushes(self, word: str) -> int:
        sol=0
        for i in range(len(word)):
            sol+=i//8+1
        return sol
        