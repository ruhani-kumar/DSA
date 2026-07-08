class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        lcp = ""
        a = strs[0]
        b = strs[-1]
        small = min(len(a),len(b))
        for i in range(small):
            if a[i]==b[i]:
                lcp+=a[i]
            else:
                break

        return lcp