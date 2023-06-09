# AddTwoNumbers

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.<br>

You may assume the two numbers do not contain any leading zero, except the number 0 itself.<br>

## Examples
### Example 1
Input: l1 = [2,4,3], l2 = [5,6,4]<br>
Output: [7,0,8]<br>
Explanation: 342 + 465 = 807.<br>

### Example 2
Input: l1 = [0], l2 = [0]<br>
Output: [0]<br>

### Example 3
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]<br>
Output: [8,9,9,9,0,0,0,1] <br>

## Constraints
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create List
        list1 = ""
        list2 = ""
        # Get values
        while l1.next:
            list1 += str(l1.val)
            l1 = l1.next
        while l2.next:
            list2 += str(l2.val)
            l2 = l2.next

        list1 += str(l1.val)
        list2 += str(l2.val)
        
        list1 = list1[::-1]
        list2 = list2[::-1]

        list3 = int(list1) + int(list2)
        list3 = str(list3)

        l3 = ListNode(val=int(list3[0]), next=None)
        for i in range(1, len(str(list3))):
            l3 = ListNode(val=int(list3[i]), next=l3)

        return l3
```

## Leetcode Link
[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
