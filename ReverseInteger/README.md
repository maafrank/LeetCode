# ReverseInteger

## Problem Description
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.<br>

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).<br>

## Examples
### Example 1
Input: x = 123<br>
Output: 321<br>

### Example 2
Input: x = -123<br>
Output: -321<br>

### Example 3
Input: x = 120<br>
Output: 21<br>

## Constraints
- -231 <= x <= 231 - 1

## Solution
```python
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        
        multiplier = 1
        if x[0] == "-":
            x = x[1:]
            multiplier = -1
            
        x = int(x[::-1])
        if x >= 2**31:
            return 0
        else:
            return x * multiplier
```

## Leetcode Link
[Reverse Integer](https://leetcode.com/problems/reverse-integer/)
