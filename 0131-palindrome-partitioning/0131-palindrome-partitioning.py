class Solution:
    def partition(self, s: str) -> list[list[str]]:
        start=0
        current=[]
        result=[]
        n=len(s)
        def backtrack(start):
            if start==n:
                result.append(current.copy())
                return
            for end in range(start+1,n+1):
                substring = s[start:end]
                if substring==substring[::-1]:
                    current.append(substring)
                    backtrack(end)
                    current.pop()
        backtrack(0)
        return result

        