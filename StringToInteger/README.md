# ReverseInteger

## Problem Description
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).<br>

The algorithm for myAtoi(string s) is as follows:<br>

Read in and ignore any leading whitespace.<br>
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.<br>
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.<br>
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).<br>
If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.<br>
Return the integer as the final result.<br>

**Note:**
- Only the space character ' ' is considered a whitespace character.
 -Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


## Examples
### Example 1
Input: s = "42"<br>
Output: 42<br>
Explanation: The underlined characters are what is read in, the caret is the current reader position.<br>
Step 1: "42" (no characters read because there is no leading whitespace)<br>
Step 2: "42" (no characters read because there is neither a '-' nor '+')<br>
Step 3: "42" ("42" is read in)<br>
The parsed integer is 42.<br>
Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.<br>

### Example 2
Input: s = "   -42"<br>
Output: -42<br>
Explanation:<br>
Step 1: "   -42" (leading whitespace is read and ignored)<br>
Step 2: "   -42" ('-' is read, so the result should be negative)<br>
Step 3: "   -42" ("42" is read in)<br>
The parsed integer is -42.<br>
Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.<br><br>

### Example 3
Input: s = "4193 with words"<br>
Output: 4193<br>
Explanation:<br>
Step 1: "4193 with words" (no characters read because there is no leading whitespace)<br>
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')<br>
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)<br>
The parsed integer is 4193.<br>
Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.<br>

## Constraints
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

## Solution
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        
        multiplier = 1
        neg = False
        pos = False
        found_digit = False
        digit = ""
        for i, letter in enumerate(s):
            
            if letter.isdigit():
                found_digit == True
                digit += letter
            elif not letter.isdigit() and len(digit) == 0 and letter != " " and letter != "-" and letter != "+": return 0
            elif len(digit) > 0 and letter == "-": return int(digit) * multiplier
            elif not s.isdigit() and len(digit) > 0 and letter == ".": return int(digit)
            elif not letter.isdigit() and len(digit) > 0: break
            elif letter == " " and (neg or pos): return 0
            elif (letter == "+" or letter == "-") and (neg or pos): return 0

            if letter == "-":
                multiplier = -1
                neg = True
            elif letter == "+": pos = True

        if neg and pos: return 0
        if digit == "": return 0

        digit = int(digit) * multiplier

        if digit <= -2**31: return -2**31
        elif digit >= 2**31 -1: return 2**31 -1
        else: return digit
```

## Leetcode Link
[String to Integer](https://leetcode.com/problems/string-to-integer-atoi/description/)
