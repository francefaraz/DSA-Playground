class Node:
  def __init__(self,val="",nxt=None,prev=None):
      self.val=val
      self.nxt=nxt
      self.prev=prev
class BrowserHistory:

  def __init__(self, homepage: str):
      self.head=Node(homepage)
      self.steps=1
      self.fsteps=1
      self.navigate=self.head

  def visit(self, url: str) -> None:
      if self.head==None:
          self.head=Node(url)
          return

      temp=self.navigate
      new_node=Node(url,prev=temp)
      temp.nxt=new_node
      self.navigate=temp.nxt
      self.steps+=1
      self.fsteps+=1
      # temp=self.head
      # self.steps+=1
      # while(temp.nxt):
      #     temp=temp.nxt
      # new_node=Node(homepage,prev=temp)
      # temp.nxt=new_node
      return        

  def back(self, steps: int) -> str:
      if not self.head:
          return "0"
      if self.steps<steps:
          return self.head.val
      temp=self.navigate
      c=self.steps

      while(temp.prev):
          if c==steps:
              break
              # self.steps=c
              # self.fsteps=self.fsteps-c
              # self.navigate=temp
              # return temp.val
          c-=1
          temp=temp.prev
      self.steps=c
      self.fsteps=self.fsteps-c
      self.navigate=temp
      return temp.val




  def forward(self, steps: int) -> str:
      if not self.head:
          return "0"
      if self.steps<steps:
          return self.head.val
      temp=self.navigate
      c=self.fsteps

      while(temp.nxt):
          if c==steps:
              self.fsteps=c
              self.steps=self.steps-c
              self.navigate=temp
              return temp.val
          c-=1
          temp=temp.nxt
      return temp.val



# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
# obj.visit("leetcode.com")
obj.visit("google.com")
# "google.com"
obj.visit("youtube.com")
obj.back(1)
obj.back(1)
obj.visit("far.com")
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)