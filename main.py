import collections


class TreeNode:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.next=None


t = TreeNode(3)
t.left = TreeNode(9)
r = TreeNode(20)
r.left = TreeNode(15)
r.right = TreeNode(7)
t.right = r

print(t.data)

# getting level number 



# level(root,xx,idx)

#levelorder traversal printing without recursion
temp = t

q = collections.deque()
q.append(temp)
print(len(q))
result = []
while q:
  q_len = len(q)
  level = []
  for _ in range(q_len):
    node = q.popleft()
    if node:
      level.append(node.data)
      q.append(node.left)
      q.append(node.right)
  if level:
    result.append(level)
print(result)

#avg level order traversal

que=[]

que.append(temp)
avg_levels=[]
while que:
  que_length=len(que)
  level=[]
  for _ in range(que_length):
    node=que.pop(0)
    if node:
      level.append(node.data)
      que.append(node.left)
      que.append(node.right)
  if level:
    # avg=f"{sum(level)//len(level)}.0000"
    avg=round((sum(level)/len(level)),5)

    avg_levels.append(avg)
print(avg_levels)



#find successor 


que=[]

que.append(temp)
key=15
while que:
  que_length=len(que)
  level=[]
  node=que.pop(0)
  if node:
    que.append(node.left)
    que.append(node.right)
  if node and node.data==key:
    break
print(que)
print("SUCCESSOR IS ",que[0].data)


#test 

que=[]
data=[]
que.append(temp)
while que:
  que_length=len(que)
  node=que.pop(0)
  if node:
    data.append(node.data)
    que.append(node.left)
    que.append(node.right)
print(data)
# print("SUCCESSOR IS ",que[0].data)



# zigzag level order traversal 

temp = t

q = collections.deque()
q.append(temp)
print(len(q))
result = []
while q:
  q_len = len(q)
  level = []
  for _ in range(q_len):
    node = q.popleft()
    if node:
      level.append(node.data)
      q.append(node.left)
      q.append(node.right)
  if level:
    result.append(level)
print(result)



#zig zag another way 


#another way 

que=collections.deque([t] if t else [])
result=[]
while que:
    level=[]
    for _ in range(len(que)):
        
        node=que.popleft()
        level.append(node.data)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
            
    result.append(level[::-1] if len(result)%2 else level)
    
print(result)

# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).


# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]


que=collections.deque([t] if t else [])
result=[]
while que:
    level=[]
    for _ in range(len(que)):
        
        node=que.popleft()
        level.append(node.data)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
            
    result.insert(0,level)
    
print(result)

# 116. Populating Next Right Pointers in Each Node

# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


que=collections.deque([t] if t else [])
result=[]
while que:
    level=[]
    for _ in range(len(que)):
        
        node=que.popleft()
        level.append(node.data)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)
    level.append('#')
    result.extend(level)
    
print(result)


# #using const memory o(1)
# # if not root:
# #     return root
# leftNode=t

# while leftNode.left:
#     curr=leftNode
#     while curr:
#         curr.left.next=curr.right
#         if curr.next:
#             curr.right.next=curr.next.left
#         curr=curr.next
#     leftNode=leftNode.left
# print(t)

#cousins of tree
# means no tree level should be same bbut cannot be under same parent
# Input: root = [1,2,3,null,4], x = 2, y = 3

# Output: false
