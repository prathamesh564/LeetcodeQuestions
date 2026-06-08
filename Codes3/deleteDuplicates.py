class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == current.next.val:
                curent.next = current.next.next
            else:
                current = current.next
        return head
