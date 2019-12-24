class Employee:
  
  def __init__(self, fname, lname, comp):
    self.fname = fname
    self.lname = lname
    self.comp = comp
    
    
   def email(self):
    return self.fname + '.' + self.lname + '@' + self.comp + '.com'
  
  def fullname(self):
    return '{} {}'.format(self.fname, self.lname)



emp_1 = Employee('alan', 'preciado', 50)
emp_2 = Employee('dania', 'arce', 60)


print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())
    
    
