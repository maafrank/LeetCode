# MergeKSortedLists

## Problem Description
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.<br>

Merge all the linked-lists into one sorted linked-list and return it.<br>

## Examples
### Example 1
Input: lists = [[1,4,5],[1,3,4],[2,6]]<br>
Output: [1,1,2,3,4,4,5,6]<br>
Explanation: The linked-lists are:<br>
[<br>
  1->4->5,<br>
  1->3->4,<br>
  2->6<br>
]<br>
merging them into one sorted list:<br>
1->1->2->3->4->4->5->6<br>

### Example 2
Input: lists = []<br>
Output: []<br>

### Example 3
Input: lists = [[]]<br>
Output: []<br>

## Constraints
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        merged_lists = []
        for l in lists:
            if l:
                merged_lists.append(l.val)
            else: continue
            while l.next:
                l = l.next
                merged_lists.append(l.val)
        
        if merged_lists == [] : return ListNode(val=merged_lists).next
        merged_lists = sorted(merged_lists, reverse=True)
        
        l1 = ListNode(val=merged_lists[0], next=None)
        for i in range(1, len(merged_lists)):
            l1 = ListNode(val=merged_lists[i], next=l1)
        
        return l1
```

## Leetcode Link
[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
