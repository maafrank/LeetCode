# MergeTwoSortedLists

## Problem Description
You are given the heads of two sorted linked lists list1 and list2.<br>

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.<br>

Return the head of the merged linked list.<br>

## Examples
### Example 1
Input: list1 = [1,2,4], list2 = [1,3,4]<br>
Output: [1,1,2,3,4,4]<br>

### Example 2
Input: list1 = [], list2 = []<br>
Output: []<br>

### Example 3
Input: list1 = [], list2 = [0]<br>
Output: [0]<br>

## Constraints
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        merged = []

        while list1 and list2:
            if list1.val == list2.val:
                merged.append(list1.val)
                merged.append(list2.val)
                list1 = list1.next
                list2 = list2.next
            elif list1.val > list2.val:
                merged.append(list2.val)
                list2 = list2.next
            elif list1.val < list2.val:
                merged.append(list1.val)
                list1 = list1.next
        
        while list1:
            merged.append(list1.val)
            list1 = list1.next
        while list2:
            merged.append(list2.val)
            list2 = list2.next

        if len(merged) == 0:
            return list1

        head = ListNode(val=merged[0])
        curr_node = head
    
        for i in range(1, len(merged)):
            new_node = ListNode(merged[i])
            curr_node.next = new_node
            curr_node = new_node
        return head
```

## Leetcode Link
[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
