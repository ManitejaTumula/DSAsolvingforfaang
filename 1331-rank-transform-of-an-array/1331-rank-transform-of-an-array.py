class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        numrank={}
        sortarr=sorted(list(set(arr)))
        rank =1
        for i in sortarr:
            numrank[i] =rank
            rank +=1
        for i in range(len(arr)):
            arr[i] =numrank[arr[i]]
        return arr
        
        