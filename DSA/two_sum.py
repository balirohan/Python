class Solution(object):
    def twoSum(self, nums, target):

        pair_idx = {}

        for idx, num in enumerate(nums):
            if target - num in pair_idx:
                return [pair_idx[target - num], idx]
            pair_idx[num] = idx


solution1 = Solution()
# print(solution1.twoSum(nums=[2,7,11,15], target=9))
# print(solution1.twoSum(nums=[3,2,4], target=6))
print(solution1.twoSum(nums=[3,3], target=6))
