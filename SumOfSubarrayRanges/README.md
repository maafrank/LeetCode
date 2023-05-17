# SumOfSubarrayRanges

## Problem Description
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.<br>

Return the sum of all subarray ranges of nums.<br>

A subarray is a contiguous non-empty sequence of elements within an array.<br>

## Examples
### Example 1
Input: nums = [1,2,3]<br>
Output: 4<br>
Explanation: The 6 subarrays of nums are the following:<br>
[1], range = largest - smallest = 1 - 1 = 0 <br>
[2], range = 2 - 2 = 0<br>
[3], range = 3 - 3 = 0<br>
[1,2], range = 2 - 1 = 1<br>
[2,3], range = 3 - 2 = 1<br>
[1,2,3], range = 3 - 1 = 2<br>
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.<br>

### Example 2
Input: nums = [1,3,3]<br>
Output: 4<br>
Explanation: The 6 subarrays of nums are the following:<br>
[1], range = largest - smallest = 1 - 1 = 0<br>
[3], range = 3 - 3 = 0<br>
[3], range = 3 - 3 = 0<br>
[1,3], range = 3 - 1 = 2<br>
[3,3], range = 3 - 3 = 0<br>
[1,3,3], range = 3 - 1 = 2<br>
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.<br>

### Example 3
Input: nums = [4,-2,-3,4,1]<br>
Output: 59<br>
Explanation: The sum of all subarray ranges of nums is 59.<br>

## Constraints
- 1 <= nums.length <= 1000
- -109 <= nums[i] <= 109

## Solution
```python
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        total = 0
        for start in range(0, len(nums)):
            minn = maxx = nums[start]
            for end in range(start+1, len(nums)):
                minn = min(minn, nums[end])
                maxx = max(maxx, nums[end])
                total += maxx - minn
        
        return total
```

## Leetcode Link
[Sum of Subarray Ranges](https://leetcode.com/problems/sum-of-subarray-ranges/)
