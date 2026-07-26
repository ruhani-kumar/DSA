class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left = 0
        right = 0
        g.sort()
        s.sort()
        while right<len(g):
            while left<len(s) and s[left]<g[right]:
                left+=1
            if left == len(s):
                break
            left+=1
            right+=1
        return right