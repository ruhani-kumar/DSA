class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)

        for s in strs:
            copy = "".join(sorted(s))
            mpp[copy].append(s)

        return list(mpp.values())