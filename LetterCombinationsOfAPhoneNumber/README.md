#  LetterCombinationsOfAPhoneNumber

## Problem Description
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.<br>

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.<br>

## Examples
### Example 1
Input: digits = "23"<br>
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]<br>

### Example 2
Input: digits = ""<br>
Output: []<br>

### Example 3
Input: digits = "2"<br>
Output: ["a","b","c"]<br>

## Constraints
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

## Solution
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # cheated for this solution. GOOGLED
        from collections import deque
        table = ["0", "1", "abc", "def", "ghi", "jkl",
                 "mno", "pqrs", "tuv", "wxyz"]
        n = len(digits)
        
        list1 = []
        q = deque()
        q.append("")
        
        while len(q) != 0:
            s = q.pop()
            
            if len(s) == n:
                list1.append(s)
            else:
                for letter in table[int(digits[len(s)])]:
                    q.append(s+letter)
        
        if list1 == [""]: return []
        return list1
```

## Leetcode Link
[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
