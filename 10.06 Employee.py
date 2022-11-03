class Employee:
    def __init__(self,firstName,lastName,idNumber,hours,wage):
        self.FirstName = firstName
        self.LastName = lastName
        self.IDNumber = idNumber
        self.HoursWorked = hours
        self.Wage = wage
    def WeeklyPay(self):
        if(self.HoursWorked > 40):
            return (40 * self.Wage) + (self.HoursWorked - 40) * 1.5 * self.Wage
        else:
            return self.HoursWorked * self.Wage
file = open("10.06 Payroll.txt")
employees =[]
for i in range(3):
    line = file.readline()
    lineData = line.strip().split(',')
    a = Employee(lineData[0].strip(),lineData[1].strip(),int(lineData[2].strip()),float(lineData[3].strip()),float(lineData[4].strip()))
    employees.append(a)
print('{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("First", "Last", "ID", "Hours", "Hourly", "Weekly"))
print('{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Name", "Name", "Number", "Worked", "Wage", "Pay"))
for a in employees:
    print('{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format(a.FirstName,a.LastName,a.IDNumber,a.HoursWorked,a.Wage,round(a.WeeklyPay(),2)))