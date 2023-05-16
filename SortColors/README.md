# SortColors

## Problem Description
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.<br>

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.<br>

You must solve this problem without using the library's sort function.<br>

## Examples
### Example 1
Input: nums = [2,0,2,1,1,0]<br>
Output: [0,0,1,1,2,2]<br>

### Example 2
Input: nums = [2,0,1]<br>
Output: [0,1,2]<br>

## Constraints
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2.

## Solution
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        colors = {}
        for num in nums:
            if num not in colors.keys():
                colors[num] = 1
            else:
                colors[num] += 1
            
        index = 0
        for i in [0, 1, 2]:
            if i in colors.keys():
                for _ in range(colors[i]):
                    nums[index] = i
                    index += 1
```

## Leetcode Link
[Sort Colors](https://leetcode.com/problems/sort-colors/)
