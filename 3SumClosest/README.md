# 3Sum

## Problem Description
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.<br>

Return the sum of the three integers.<br>

You may assume that each input would have exactly one solution.<br>

## Examples
### Example 1
Input: nums = [-1,2,1,-4], target = 1<br>
Output: 2<br>
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).<br>

### Example 2
Input: nums = [0,0,0], target = 1<br>
Output: 0<br>
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).<br>

## Constraints
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

## Solution
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums = sorted(nums)
        tot = 10**9
        for i in range(0, len(nums)):
            
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total - target == 0:
                    return total
                elif abs(target - total) < abs(target - tot):
                    tot = total
                    
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
        return tot
```

## Leetcode Link
[3Sum Closest](https://leetcode.com/problems/3sum-closest/)
