# ReorderDataInLogFiles

## Problem Description
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.<br>

There are two types of logs:<br>

- Letter-logs: All words (except the identifier) consist of lowercase English letters.<br>
- Digit-logs: All words (except the identifier) consist of digits.<br>
Reorder these logs so that:<br>

The letter-logs come before all digit-logs.<br>
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.<br>
The digit-logs maintain their relative ordering.<br>
Return the final order of the logs.<br>

## Examples
### Example 1
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]<br>
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]<br>
Explanation:<br>
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".<br>
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".<br>

### Example 2
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]<br>
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]<br>

## Constraints
- 1 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- All the tokens of logs[i] are separated by a single space.
- logs[i] is guaranteed to have an identifier and at least one word after the identifier.

## Solution
```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs1 = {}
        letter_logs2 = {}
        digit_logs  = []
        for log in logs:
            log_arr = log.split(" ")
            if log_arr[1].isdigit():
                digit_logs.append(log)
            else:
                if log_arr[0] not in letter_logs1.keys():
                    letter_logs1[log_arr[0]] = log.replace(log_arr[0], "")
                if log.replace(log_arr[0] + " ", "") not in letter_logs2.keys():
                    letter_logs2[log.replace(log_arr[0] + " ", "", 1)] = log_arr[0]
                else:
                    letter_logs2[log.replace(log_arr[0] + " ", "", 1)] += "~" + log_arr[0]
                    
        letter_logs = []
        for key in sorted(letter_logs2.keys()):
            if "~" in letter_logs2[key]:
                for item in sorted(letter_logs2[key].split("~")):
                    letter_logs.append(item + " " + key)
            else:
                letter_logs.append(letter_logs2[key] + " " + key)
        return letter_logs + digit_logs
```

## Leetcode Link
[Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)
