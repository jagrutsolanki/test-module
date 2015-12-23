class Employee:
 empCount = 0
 
 def __init__(self,name,salary):
  self.name = name
  self.salary = salary
  Employee.empCount += 1
 def displayCount(self):
  print "Total employee %d" % Employee.empCount

 def displayEmployee(self):
  print "Name:",self.name,"salary:",self.salary 

emp1 = Employee("Zara",20000)
emp2 = Employee("hardik",30000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount
