class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        numberset=set(nums)
        max_num=max(nums)
        min_num=min(nums)
        miss=[]
        for i in range(min_num,max_num+1):
            if i not in numberset:
                miss.append(i)
        return miss
        