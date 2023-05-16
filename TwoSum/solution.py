 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            tar = target - num1
            try:
                j = nums.index(tar)
                if i == j: continue
                return [i, j]
            except Exception as e:
                continue
