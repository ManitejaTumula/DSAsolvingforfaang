class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack=[]
        result={}
        n=len(nums2)
        for i in range(n-1,-1,-1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                result[nums2[i]] = stack[-1]
            else:
                result[nums2[i]] = -1
            stack.append(nums2[i])
        return [result[num] for num in nums1]


        