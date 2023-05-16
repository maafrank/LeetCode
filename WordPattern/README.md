# WordPattern

## Problem Description
Given a pattern and a string s, find if s follows the same pattern.<br>

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.<br>

## Examples
### Example 1
Input: pattern = "abba", s = "dog cat cat dog"<br>
Output: true<br>

### Example 2
Input: pattern = "abba", s = "dog cat cat fish"<br>
Output: false<br>

### Example 3
Input: pattern = "aaaa", s = "dog cat cat dog"<br>
Output: false<br>

## Constraints
- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.

## Solution
```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split(" ")

        p1 = {}
        p2 = {}
        for i in range(0, len(s)):
            if pattern[i] not in p.keys():
                p[pattern[i]] = s[i]
            else:
                if p[pattern[i]] != s[i]:
                    return False
        return True
```

## Leetcode Link
[Word Pattern](https://leetcode.com/problems/word-pattern/)
