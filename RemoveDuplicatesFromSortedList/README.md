# RemoveDuplicatesFromSortedList

## Problem Description
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.<br>

## Examples
### Example 1
Input: head = [1,1,2]<br>
Output: [1,2]<br>

### Example 2
Input: head = [1,1,2,3,3]<br>
Output: [1,2,3]<br>

## Constraints
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        prev_node = head
        curr_node = head.next
        
        while curr_node:
            if curr_node.val == prev_node.val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        
        return head
```

## Leetcode Link
[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
