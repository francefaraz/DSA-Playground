class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def create_linked_list(lst):
  head = ListNode(lst[0])
  current = head
  for item in lst[1:]:
      current.next = ListNode(item)
      current = current.next
  return head

def print_linked_list(head):
  current = head
  while current:
      print(current.val, end=" ")
      current = current.next
  print()

# Given lists
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# Creating linked lists
head1 = create_linked_list(list1)
head2 = create_linked_list(list2)

# Printing linked lists
print("Linked List 1:")
print_linked_list(head1)
print("Linked List 2:")
print_linked_list(head2)
