# CountAndSay

## Problem Description
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:<br>

countAndSay(1) = "1"<br>
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.<br>
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.<br>

For example, the saying and conversion for digit string "3322251":<br>
Given a positive integer n, return the nth term of the count-and-say sequence.<br>

## Examples
### Example 1
Input: n = 1<br>
Output: "1"<br>
Explanation: This is the base case.<br>

### Example 2
Input: n = 4<br>
Output: "1211"<br>
Explanation:<br>
countAndSay(1) = "1"<br>
countAndSay(2) = say "1" = one 1 = "11"<br>
countAndSay(3) = say "11" = two 1's = "21"<br>
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"<br>

## Constraints
- 1 <= n <= 30

## Solution
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def convert (say: str) -> str:
            cvt = ""
            cnt = 0
            num = say[0]
            while say:
                if say[0] == num:
                    cnt += 1
                else:
                    cvt += str(cnt) + num
                    num = say[0]
                    cnt = 1
                say = say[1:]
                
            cvt += str(cnt) + num
            return cvt
        
        cvt = convert("1")
        for _ in range(1, n-1):
            cvt = convert(cvt)
            
        return cvt
```

## Leetcode Link
[Count and Say](https://leetcode.com/problems/count-and-say/)
