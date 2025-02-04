# Iterative way 



class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to reverse linked list
# using 3 pointer approach
def reverseLinkedListLoop(head):

    # Initialize 'temp' at the
    # head of the linked list
    temp = head

    # Initialize 'prev' to None,
    # representing the previous node 
    prev = None

    while temp is not None:
        # Store the next node in 'front'
        # to preserve the reference
        front = temp.next
        # Reverse the direction of the current
        # node's 'next' pointer to point to 'prev'
        temp.next = prev
        # Move 'prev' to the current 
        # node, for the next iteration
        prev = temp
        # Move 'temp' to 'front' node
        # advancing traversal
        temp = front

    # Return the new head
    # of the reversed linked list
    return prev

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverseLinkedListLoop(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)









# recursive way 


# Function to reverse a singly
# linked list using a recursion
def reverse_linked_list(head):
    # Base case:
    # If the linked list is empty or has only one node,
    # return the head as it is already reversed.
    if head is None or head.next is None:
        return head

    # Recursive step:
    # Reverse the linked list starting from the second node (head.next).
    new_head = reverse_linked_list(head.next)

    # Save a reference to the node following
    # the current 'head' node.
    front = head.next

    # Make the 'front' node point to the current
    # 'head' node in the reversed order.
    front.next = head

    # Break the link from the current 'head' node
    # to the 'front' node to avoid cycles.
    head.next = None

    # Return the 'new_head,' which is the new
    # head of the reversed linked list.
    return new_head


# Function to print the linked list
# def print_linked_list(head):
#     temp = head
#     while temp is not None:
#         print(temp.data, end=" ")
#         temp = temp.next
#     print()

# Create a linked list with
# values 1, 3, 2, and 4
head = Node(1)
head.next = Node(3)
head.next.next = Node(2)
head.next.next.next = Node(4)

# Print the original linked list
print("Original Linked List:", end=" ")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

# Print the reversed linked list
print("Reversed Linked List:", end=" ")
print_linked_list(head)

''' 
Complexity Analysis
Time Complexity: O(N) This is because we traverse the linked list twice: once to push the values onto the stack, and once to pop the values and update the linked list. Both traversals take O(N) time.

Space Complexity : O(1) No additional space is used explicitly for data structures or allocations during the linked list reversal process. However, it’s important to note that there is an implicit use of stack space due to recursion. This recursive stack space stores function calls and associated variables during the recursive traversal and reversal of the linked list. Despite this, no extra memory beyond the program’s existing execution space is allocated, hence maintaining a space complexity of O(1).
'''