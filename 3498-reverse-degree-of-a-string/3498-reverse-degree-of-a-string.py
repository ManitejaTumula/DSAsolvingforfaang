class Solution:
    def reverseDegree(self, s: str) -> int:
      ans=0
      index=1
      for ch in s:
        ans+= (123 - ord(ch)) * index
        index+=1
      return ans