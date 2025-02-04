from typing import NamedTuple 
from dataclasses import dataclass 
class Person(NamedTuple): 
  name: str  
  age: int

@dataclass
class Person1(NamedTuple): 
  name: str  
  age: int



def hello(a:Person):
  print(a)


def hello1(a:Person1):
  print(a)


hello({'name':"far",'city':'bangalore'})
hello({'name':"far",'city':'bangalore'})
