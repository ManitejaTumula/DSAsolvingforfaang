class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        current =[]
        result=[]
        def backtrack(index,target):
            if target == 0:
                result.append(current.copy())
                return
            if target < 0:
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                current.append(candidates[i])
                backtrack(i+1, target - candidates[i])
                current.pop()
        backtrack(0,target)
        return result