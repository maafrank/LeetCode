# PalindromeNumber

## Problem Description
Given an integer x, return true if x is a palindrome, and false otherwise.<br>

## Examples
### Example 1
Input: x = 121<br>
Output: true<br>
Explanation: 121 reads as 121 from left to right and from right to left.<br>

### Example 2
Input: x = -121<br>
Output: false<br>
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.<br>

### Example 3
Input: x = 10<br>
Output: false<br>
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.<br>

## Constraints
- -2^31 <= x <= 2^31 - 1

## Solution
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0] == "-": return False
        return x == x[::-1]
```

## Leetcode Link
[Palindrome Number](https://leetcode.com/problems/palindrome-number/)
