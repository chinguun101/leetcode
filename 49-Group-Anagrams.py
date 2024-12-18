class Solution(object):
    def groupAnagrams(self, strs):
        \\\
        :type strs: List[str]
        :rtype: List[List[str]]
        \\\
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            
            for l in s:
                count[ord(l)-ord('a')] += 1

            d[tuple(count)].append(s)
        return d.values()