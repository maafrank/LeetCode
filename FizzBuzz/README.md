# FizzBuzz

## Problem Description
Given an integer n, return a string array answer (1-indexed) where:<br>

- answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
- answer[i] == "Fizz" if i is divisible by 3.
- answer[i] == "Buzz" if i is divisible by 5.
- answer[i] == i (as a string) if none of the above conditions are true.<br>

## Examples
### Example 1
Input: n = 3<br>
Output: ["1","2","Fizz"]<br>

### Example 2
Input: n = 5<br>
Output: ["1","2","Fizz","4","Buzz"]<br>

### Example 3
Input: n = 15<br>
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]<br>

## Constraints
- 1 <= n <= 10^4

## Solution
```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        answer = []
        for i in range(1,n+1):
            if (not i % 3) and (not i % 5):
                answer.append("FizzBuzz")
            elif (not i % 3):
                answer.append("Fizz")
            elif (not i % 5):
                answer.append("Buzz")
            else: 
                answer.append(str(i))
        return answer
```

## Leetcode Link
[Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)
