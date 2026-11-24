class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            n = "".join(sorted(i))
            if n not in seen:
                seen[n] = [i]
            else:
                seen[n].append(i)

        return list(seen.values())
        