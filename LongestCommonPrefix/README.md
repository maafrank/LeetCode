# RomanToInteger

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings.<br>

If there is no common prefix, return an empty string "".<br>

## Examples
### Example 1
Input: strs = ["flower","flow","flight"]<br>
Output: "fl"<br>

### Example 2
Input: strs = ["dog","racecar","car"]<br>
Output: ""<br>
Explanation: There is no common prefix among the input strings.<br>

## Constraints
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

## Solution
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if strs[0] == "":
            return ""
        
        index = 0
        sub_string = ""
        longest_sub_string = ""
        while True:
            if index >= len(strs[0]):
                return strs[0]
            sub_string += strs[0][index]
            for word in strs:
                if word.startswith(sub_string):
                    longest_sub_string = sub_string
                else:
                    return longest_sub_string[:-1]
            index += 1
```

## Leetcode Link
[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
