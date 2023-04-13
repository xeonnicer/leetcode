"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        _map = {}
        for str in strs:
            key = ''.join(sorted(str))
            _map.setdefault(key, []).append(str)
        return list(_map.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = Solution().groupAnagrams(strs)
print(ans)