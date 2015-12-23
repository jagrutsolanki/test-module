class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

emp1 = Employee("Varun",2000)
emp2 = Employee("Varshal",3000)
emp3 = Employee("Harshal",4000)
emp4 = Employee("Trushal",5000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()

print "Total number of Employee %d" % Employee.empCount
