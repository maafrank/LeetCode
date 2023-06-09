# MedianOfTwoSortedArrays

## Problem Description
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.<br>

The overall run time complexity should be O(log (m+n)).<br>

## Examples
### Example 1
Input: nums1 = [1,3], nums2 = [2]<br>
Output: 2.00000<br>
Explanation: merged array = [1,2,3] and median is 2.<br>

### Example 2
Input: nums1 = [1,2], nums2 = [3,4]<br>
Output: 2.50000<br>
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.<br>

## Constraints
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- 106 <= nums1[i], nums2[i] <= 106

## Solution
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        
        if len(merged_array) % 2 == 0: 
            # even
            return (merged_array[len(merged_array)//2] + merged_array[(len(merged_array)//2) - 1]) / 2
        else:
            # odd
            return merged_array[len(merged_array)//2]
```

## Leetcode Link
[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
