class Employee:

    employee_count=101

    def __init__(self):
        self.name=input("Enter Name: ")
        self.salary=input("Enter Salary: ")
        self.designation=input("Enter Designation: ")
        self.emp_ID="E"+str(Employee.employee_count)
        Employee.employee_count+=1

    def show_name(self):
        print("EmpId: ",self.emp_ID)
        print("Name:",self.name)
        print("Salary: ",self.salary)
        print("Designation: ",self.designation)

    @classmethod
    def total_count(cls):
        print("Employee Count: ",(Employee.employee_count-101))


if __name__=="__main__":
    n=int(input("Enter Number of Employees you want to add: "))
    objl=[]
    for i in range(n):
        objl.append(Employee())
    print(objl)
    objl[1].show_name()
    print(Employee.total_count())



