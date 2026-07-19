class Solution:
    def smallestSubsequence(self, s: str) -> str:
        seen=set()
        stack=[]
        for i,char in enumerate(s):
            if char in seen:
                continue
            last_occurence ={c:i for i,c in enumerate(s)}
            while stack and stack[-1] > char and last_occurence[stack[-1]] > i:
                removestack=stack.pop()
                seen.remove(removestack)
            stack.append(char)
            seen.add(char)
        return "".join(stack)


        