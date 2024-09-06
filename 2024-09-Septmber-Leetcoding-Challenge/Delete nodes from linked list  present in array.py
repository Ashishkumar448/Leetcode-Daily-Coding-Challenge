class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums list to a set for O(1) look-up time
        num_set = set(nums)
        
        # Dummy node to handle edge cases easily
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy
        
        # Traverse the linked list
        while current:
            if current.val in num_set:
                # Delete the current node by skipping it
                prev.next = current.next
            else:
                # Move prev to current node if not deleted
                prev = current
            # Move to the next node
            current = current.next
        
        # Return the head of the modified list
        return dummy.next
