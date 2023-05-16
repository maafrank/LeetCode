# FirstMissingPositive

## Problem Description
Given an unsorted integer array nums, return the smallest missing positive integer.<br>

You must implement an algorithm that runs in O(n) time and uses constant extra space.<br>

## Examples
### Example 1
Input: nums = [1,2,0]<br>
Output: 3<br>
Explanation: The numbers in the range [1,2] are all in the array.<br>

### Example 2
Input: nums = [3,4,-1,1]<br>
Output:2 <br>
Explanation: 1 is in the array but 2 is missing.<br>

### Example 3
Input: nums = [7,8,9,11,12]<br>
Output: 1<br>
Explanation: The smallest positive integer 1 is missing.<br>

## Constraints
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

## Solution
```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #remove duplicates 
        nums = list(set(nums))

        # remove everything less than 1
        for ele in nums: 
            if ele < 1: nums.remove(ele)

        # check for empty list
        if not len(nums): return 1

        # make sure we have every number
        for i, ele in enumerate(nums):
            if i+1 == ele:continue
            elif i+1 not in nums:return i+1

        return i+2
```

## Leetcode Link
[First Missing Positive](https://leetcode.com/problems/first-missing-positive/)
