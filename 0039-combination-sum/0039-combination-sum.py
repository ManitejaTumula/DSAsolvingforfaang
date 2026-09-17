class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        current=[]
        result=[]
        n=len(candidates)
        def backtracking(index,target):
            if target == 0:
                result.append(current.copy())
                return
            if target < 0:
                return
            for i in range(index,n):
                current.append(candidates[i])
                backtracking(i, target - candidates[i])
                current.pop()
        backtracking(0,target)
        return result
