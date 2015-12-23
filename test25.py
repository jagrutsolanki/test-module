class SchoolMember:
	''' Represent any school Member'''
def __init__(self,name,age):
 self.name = name
 self.age = age
 print '(Initialize schoolMember:())'.format(self.name)

def tell(self):
 ''' Tell my details'''
 print 'Name:"()" Age:"()"'.format(self.name,self.age)

class Teacher(SchoolMember):
 ''' Represent Teacher'''
 def __init__(self,name,age,salary):
  ScholMember. __init__(self,name,age)
  self.salary = salary
  print '(Initialized Teacher:())'.format(self.name)
 
 def tell(self):
  SchoolMember.tell(self)
  print 'salary: "{:d}"'.format(self.salary) 
