# LongestSubstringWithoutRepeatingCharacters

## Problem Description
Given a string s, find the length of the longest 
substring without repeating characters.<br>

## Examples
### Example 1
Input: s = "abcabcbb"<br>
Output: 3<br>
Explanation: The answer is "abc", with the length of 3.<br>

### Example 2
Input: s = "bbbbb"<br>
Output: 1<br>
Explanation: The answer is "b", with the length of 1.<br>

### Example 3
Input: s = "pwwkew"<br>
Output: 3<br>
Explanation: The answer is "wke", with the length of 3.<br>
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.<br>

## Constraints
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

## Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest_sub_string = []
        for i, start in enumerate(s):
            sub_string = []
            sub_string.append(start)
            
            for j in range(i+1, len(s)):
                if start != s[j] and s[j] not in sub_string:
                    sub_string.append(s[j])
                else: break

            if len(sub_string) > len(longest_sub_string):
                longest_sub_string = sub_string
            
        return len(longest_sub_string)
```

## Leetcode Link
[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
