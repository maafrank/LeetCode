# TwoSum

## Problem Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. <br>
You may assume that each input would have exactly one solution, and you may not use the same element twice. <br>
You can return the answer in any order. <br>

## Examples
### Example 1
Input: nums = [2,7,11,15], target = 9 <br>
Output: [0,1] <br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. <br>

### Example 2
Input: nums = [3,2,4], target = 6 <br>
Output: [1,2] <br>

### Example 3
Input: nums = [3,3], target = 6 <br>
Output: [0,1] <br>

### Solution
```python
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
```

## Leetcode Link
[Two Sum](https://leetcode.com/problems/two-sum/)
