# RomanToInteger

## Problem Description
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.<br>

Symbol=       Value<br>
I=             1<br>
V=             5<br>
X=             10<br>
L=             50<br>
C=             100<br>
D=             500<br>
M=             1000<br>
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.<br>

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:<br>

- I can be placed before V (5) and X (10) to make 4 and 9. <br>
- X can be placed before L (50) and C (100) to make 40 and 90. <br>
- C can be placed before D (500) and M (1000) to make 400 and 900.<br>

Given a roman numeral, convert it to an integer.<br>

## Examples
### Example 1
Input: s = "III"<br>
Output: 3<br>
Explanation: III = 3.<br>

### Example 2
Input: s = "LVIII"<br>
Output: 58<br>
Explanation: L = 50, V= 5, III = 3.<br>

### Example 3
Input: s = "MCMXCIV"<br>
Output: 1994<br>
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.<br>

## Constraints
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Solution
```python
class Solution:
    def __init__(self):
        self.roman_dict = {"I" : 1, 
                           "V" : 5, 
                           "X" : 10, 
                           "L" : 50, 
                           "C" : 100, 
                           "D" : 500, 
                           "M" : 1000,
                           "CD" : 400,
                           "CM" : 900, 
                           "XL" : 40, 
                           "XC" : 90, 
                           "IV" : 4, 
                           "IX" : 9}
        
    def romanToInt(self, s: str) -> int:
        value = 0
        found = False
        for i in range(1, len(s)):
            
            if found:
                found = False
                continue
                
            if s[i-1:i+1] in self.roman_dict.keys():
                value += self.roman_dict[s[i-1:i+1]]
                found = True
            else:
                value += self.roman_dict[s[i-1]]
                
        if not found:
            value += self.roman_dict[s[-1]]
        return value
```

## Leetcode Link
[Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
