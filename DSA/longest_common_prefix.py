class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in range(len(strs)):
            while not strs[i].startswith(prefix) and prefix:
                prefix = prefix[:-1]
        return prefix

solution1 = Solution()
# print(solution1.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(solution1.longestCommonPrefix(strs = ["dog","racecar","car"]))