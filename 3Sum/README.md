# 3Sum

## Problem Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.<br>

Notice that the solution set must not contain duplicate triplets.<br>

## Examples
### Example 1
nput: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.<br>

### Example 2
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.<br>

### Example 3
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

## Constraints
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

## Solution
```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        triplets = []
        
        for i in range(0, len(nums)):
            
            j = i + 1
            k = len(nums) -1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                elif total == 0:
                    item = sorted([nums[i], nums[j], nums[k]])
                    if item not in triplets:
                        triplets.append(item)
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return triplets
```

## Leetcode Link
[3Sum](https://leetcode.com/problems/3sum/)
