# LongestPalindromicSubstring

## Problem Description
Given a string s, return the longest 
palindromic substring in s.<br>

## Examples
### Example 1
Input: s = "babad"<br>
Output: "bab"<br>
Explanation: "aba" is also a valid answer.<br>

### Example 2
Input: s = "cbbd"<br>
Output: "bb"<br>

## Constraints
- 1 <= s.length <= 1000
- s consist of only digits and English letters.

## Solution
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest=""
        for start in range(0, len(s)):
            for end in range(start, len(s)+1):
                substring = s[start:end]
                if substring == substring[::-1]:
                    if len(substring) > len(longest):
                        longest = substring
        return longest
```

## Leetcode Link
[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
