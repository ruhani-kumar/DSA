class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 0
        num = 0
        for d in reversed(digits):
            num += (10**i) * d
            i+=1
        res = num+1
        return ([int(x) for x in str(res)])
        