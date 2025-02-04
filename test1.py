def listSum(numbers):
  if not numbers:
    return 0
  else:
    (f, rest) = numbers
    return f + listSum(rest)

myList = (1, (2, (3, None)))
total = listSum(myList)

class far:

    def __init__(self):
        self.f=1
    def print(self):
        print(self.f)
f=far()
f.print()


class Node:

    def __init__(self,val=0,nxt=None):
        self.val=val
        self.nxt=nxt



class MyLinkedList:

    def __init__(self):

        self.head=None



    def get(self, index: int):
        print(self.head.val)
        temp=self.head
        count=0
        while(temp):
            if count==index:
                return temp.val

            temp=temp.nxt
        return -1


    def addAtHead(self, val: int):
        new_node=Node(val,self.head)
        self.head=new_node
        print(self.head,"add head")
        return


    def addAtTail(self, val: int):
        new_node=Node(val)
        if self.head==None:
            print('here')
            self.head=new_node
        temp=self.head
        while(temp.nxt):
            temp=temp.nxt
        temp.nxt=new_node

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,3