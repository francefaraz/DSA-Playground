def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

if head is None:
    return []
dict_ll={}
count=0
temp=head
while temp:
    dict_ll[count]=temp
    temp=temp.next
    count+=1
return dict_ll[count//2]
#  one approch is above one and another approch using pointers 
def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return []
    
    f=s=head
    while f and f.next:
        s=s.next
        f=f.next.next
    return s