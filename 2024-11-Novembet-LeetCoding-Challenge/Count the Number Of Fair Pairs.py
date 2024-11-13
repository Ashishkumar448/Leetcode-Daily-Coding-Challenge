class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_last(self, node):
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

# Helper function to get the length of a linked list
def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

# Helper function to move a pointer forward by k nodes
def move_forward_by_k(head, k):
    while k > 0 and head:
        head = head.next
        k -= 1
    return head

# Function to find intersection point in Y shaped Linked Lists
def intersect_point(head1, head2):
    len1 = get_length(head1)
    len2 = get_length(head2)

    # Calculate the difference in lengths
    diff = abs(len1 - len2)

    # Adjust the starting point of the longer list
    if len1 > len2:
        head1 = move_forward_by_k(head1, diff)
    else:
        head2 = move_forward_by_k(head2, diff)

    # Traverse both lists together to find the intersection point
    while head1 and head2:
        if head1 == head2:
            return head1.data  # Intersection point found
        head1 = head1.next
        head2 = head2.next

    return -1  # No intersection found

# Driver code to create lists and find intersection
# Use intersect_point(llist1.head, llist2.head) to find intersection point
