from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 设置滑动窗口队列，window
        window = deque()
        max_length = 0
        # curr_length = 0
        for i in s:
            window.append(i)
            if len(window) == len(set(window)):
                max_length = max(max_length,len(window))
            else:
                while len(window) > len(set(window)):
                    window.popleft()
        # 已经覆盖了所有元素，return 长度
        # load 元素，扩张window
        # 判断是否合规。
        # 合规，长度加一
        # 不合规，移动窗口（左边减少1）
        #
        return max_length



sln = Solution()
res = sln.lengthOfLongestSubstring("nfpdmpi")
print(res)