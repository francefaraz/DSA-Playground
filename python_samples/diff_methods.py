class students:

  school="HARVARD"

  def __init__(self,m):
    self.m=m

  def set(self,m):
    self.m=m

  def get(self):
    return self.m

  @classmethod
  def itsclassmethod1(se):
    print(se,dir(se))
    print(se.school)
    return None

  @classmethod
  def itsclassmethod(ar):
    # print(students,dir(students))
    # print(students.school)
    return None 

  @staticmethod
  def staicmethodthis():
    print(students,dir(students))

    print("hello this is static method no need to create a object")
    print(students.school)


s=students(5)
s.get()
s.set(10)
s.get()
students.itsclassmethod1()
students.itsclassmethod()
students.staicmethodthis()