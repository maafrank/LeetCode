# GroupAnagrams

## Problem Description
Given an array of strings strs, group the anagrams together. You can return the answer in any order.<br>

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.<br>

## Examples
### Example 1
Input: strs = ["eat","tea","tan","ate","nat","bat"]<br>
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]<br>

### Example 2
Input: strs = [""]<br>
Output: [[""]]<br>

### Example 3
Input: strs = ["a"]<br>
Output: [["a"]]<br>

## Constraints
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

## Solution
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in word_dict.keys():
                word_dict[sorted_word] = [word]
            else:
                word_dict[sorted_word].append(word)

        groups = []
        for value in word_dict.values():
            groups.append(value)

        return groups
```

## Leetcode Link
[Group Anagrams](https://leetcode.com/problems/group-anagrams/)
