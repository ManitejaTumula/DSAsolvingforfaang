class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        current=[]
        result=[]
        n=len(nums)
        def backtrack(index):
            if index == n:
                result.append(current.copy())
                return
            current.append(nums[index])
            backtrack(index+1)
            current.pop()
            backtrack(index+1)
        backtrack(0)
        return result
            



        