from typing import List

class Employee:
   def __init__(self, firstname, lastname, idnumber, wage, hoursworked = 0):
       self.firstname = firstname
       self.lastname = lastname
       self.idnumber = int(idnumber)
       self.hoursworked = float(hoursworked)
       self.wage = float(wage)
   def WeeklyPay(self):
       if self.hoursworked > 40:
           return self.wage * 40 + self.wage * 1.5 * (self.hoursworked - 40)
       return self.hoursworked * self.wage

def find_employee(employees : List[Employee], employees_pay):
   for i in range(len(employees)):
       if employees_pay == employees[i].idnumber:
           return i
   return -1

if __name__ == '__main__':
   file = '11.02 Employees.txt'
   hours_file = '11.02 Hours.txt'
   hours = open(file)
   employees = []
   for line in hours:
       line = line.strip('\n').split(',')
       firstname, lastname, idnumber, wage = line[0], line[1], int(line[2]), float(line[3])
       employee = Employee(firstname, lastname, idnumber, wage)
       employees.append(employee)
   hours = open(hours_file)
   for line in hours:
       line = line.strip('\n').split(',')
       idnumber, hours = int(line[0]), float(line[1])
       index = find_employee(employees, idnumber)
       if index != -1:
           employees[index].hoursworked = hours
   print('{0:13s}{1:13s}{2:10s}  {3:14s}  {4:14s}{5:14s}'.format('First Name', 'Last Name', 'ID Number', 'Hours Worked','Hourly Wage', 'Weekly Pay'))
   for e in employees:
       print('{0:13s}{1:13s}{2:10d}{3:14.2f}{4:14.2f}{5:14.2f}'.format(e.firstname, e.lastname, e.idnumber,e.hoursworked, e.wage, e.WeeklyPay()))