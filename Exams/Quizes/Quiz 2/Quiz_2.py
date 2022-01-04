#Quiz 2
#Md Danial Islam
#20101534
#Sec: 01

class Student:
  def __init__(self,name=""):
    self.name = name
    self.courses = {}
  def setName(self,name):
    self.name = name

  def addCourse(self,*course):
    if (self.name == ""):
      print("A course can not be added without student name")
    else:
      if ( course[1] in self.courses.keys() ):
        self.courses[course[1]].append(course[0])
      else:
        self.courses[course[1]] = [course[0]]

  def printDetail(self):
    print("Number of Course(s): {}\nStudent Name: {}".format(len(self.courses),self.name))
    for c_name,c_code in self.courses.items():
      code = ""
      for item in c_code:
        code += item+", "
      code = code[:-2]
      print(c_name +": "+ code)

s1 = Student()
print("=================================")
s1.addCourse("CSE110", "Computer Science")
print("=================================")
s1.setName("Bob")
s1.addCourse("CSE110", "Computer Science")
s1.printDetail()
print("=================================")
s2 = Student("Carol")
s2.addCourse("CSE111", "Computer Science")
s2.addCourse("MAT110", "Mathematics")
print("=================================")
s2.printDetail()
s2.addCourse("CSE230", "Computer Science")
print("=================================")
s2.printDetail()
print("=================================")