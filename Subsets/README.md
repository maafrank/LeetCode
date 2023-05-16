# Subsets

## Problem Description
Given an integer array nums of unique elements, return all possible subsets (the power set).<br>

The solution set must not contain duplicate subsets. Return the solution in any order.<br>

## Examples
### Example 1
Input: nums = [1,2,3]<br>
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]<br>

### Example 2
Input: nums = [0]<br>
Output: [[],[0]]<br>

## Constraints
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique.

## Solution
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, [], nums, 0)
        return res
    
    def backtrack(self, res, subset, nums, start):
        res.append(subset[:])
        for i in range(start, len(nums)):
            subset.append(nums[i])
            self.backtrack(res, subset, nums, i+1)
            subset.pop()
```

## Leetcode Link
[Subsets](https://leetcode.com/problems/subsets/)
