class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == current.next.val:
                cur.next = current.next.next
            else:
                cur = current.next
        return head
