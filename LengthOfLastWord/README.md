# LengthOfLastWord

## Problem Description
Given a string s consisting of words and spaces, return the length of the last word in the string.<br>

A word is a maximal substring consisting of non-space characters only.<br>

## Examples
### Example 1
Input: s = "Hello World"<br>
Output: 5<br>
Explanation: The last word is "World" with length 5.<br>

### Example 2
Input: s = "   fly me   to   the moon  "<br>
Output: 4<br>
Explanation: The last word is "moon" with length 4.<br>

### Example 3
Input: s = "luffy is still joyboy"<br>
Output: 6<br>
Explanation: The last word is "joyboy" with length 6.<br>

## Constraints
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '.
- There will be at least one word in s.

## Solution
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
```

## Leetcode Link
[Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
