while True:

    print("============================================================================")
    print("~~~~~~~~~~~~~~~~  EMPLOYEE MANAGEMENT SYSTEM ~~~~~~~~~~~~~~~~~")
    print("============================================================================")
    print("1. CREATE AN EMPLOYEE: ")
    print("2. CREATE A MANAGER: ")
    print("3. CREATE A DEVELOPER: ")
    print("4  CHECK CLASS: ")
    print("5. SHOW DETAILS: ")
    print("6 EXIT")
    choice=int(input("enter your choice from 1 to 6: "))

    if choice==1:
        class Employee:
            def __init__(self, emp_id, name, age, salary):
                self.emp_id = emp_id
                self.name = name
                self.age = age
                self.salary = salary
            def get_id(self):
                return self.emp_id
            def get_name(self):
                return self.name
            def get_age(self):
                return self.age
            def get_salary(self):
                return self.salary
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        salary = float(input("Enter Employee Salary: "))
        employee = Employee(emp_id, name, age, salary)
        print("Employee created successfully!") 

    elif choice==2:
        class Manager(Employee):
            def __init__(self, emp_id, name, age, salary, department):
                super().__init__(emp_id, name, age, salary)
                self.department = department
            def display_department(self):
                super().display()
                print(f"Department: {self.department}")
        emp_id = input("Enter Manager ID: ")
        name = input("Enter Manager Name: ")
        age = int(input("Enter Manager Age: "))
        salary = float(input("Enter Manager Salary: "))
        department = input("Enter Manager Department: ")
        manager = Manager(emp_id, name, age, salary, department)
        print("Manager created successfully!")
    elif choice==3:
        class Developer(Employee):
            def __init__(self, emp_id, name, age, salary, programming_language):
                super().__init__(emp_id, name, age, salary)
                self.programming_language = programming_language
            def display(self):
                super().display()
                print(f"Programming Language: {self.programming_language}")
        emp_id = input("Enter Developer ID: ")
        name = input("Enter Developer Name: ")
        age = int(input("Enter Developer Age: "))
        salary = float(input("Enter Developer Salary: "))
        programming_language = input("Enter Developer Programming Language: ")
        developer = Developer(emp_id, name, age, salary, programming_language)
        print("Developer created successfully!")

    elif choice==4:
        class Employee:
            def __init__(self, emp_id, name, age, salary):
                self.emp_id = emp_id
                self.name = name
                self.age = age
                self.salary = salary
        class Manager(Employee):
            def __init__(self, emp_id, name, age, salary, department):
                super().__init__(emp_id, name, age, salary)
                self.department = department
        class Developer(Employee):
            def __init__(self, emp_id, name, age, salary, programming_language):
                super().__init__(emp_id, name, age, salary)
                self.programming_language = programming_language

        emp = Employee("E001", "Alice", 30, 50000)
        mgr = Manager("M001", "Bob", 40, 70000, "Sales")
        dev = Developer("D001", "Charlie", 25, 60000, "Python")

        print(f"Is mgr an instance of Employee? {isinstance(mgr, Employee)}")
        print(f"Is dev an instance of Manager? {isinstance(dev, Manager)}")
        print(f"Is emp an instance of Developer? {isinstance(emp, Developer)}")

    elif choice==5: 
        print("Employee Details:")
        print(f"ID: {employee.get_id()}, Name: {employee.get_name()}, Age: {employee.get_age()}, Salary: {employee.get_salary()}")

        print("\nManager Details:")
        print(f"ID: {manager.get_id()}, Name: {manager.get_name()}, Age: {manager.get_age()}, Salary: {manager.get_salary()}, Department: {manager.department}")

        print("\nDeveloper Details:")
        print(f"ID: {developer.get_id()}, Name: {developer.get_name()}, Age: {developer.get_age()}, Salary: {developer.get_salary()}, Programming Language: {developer.programming_language}")

    elif choice==6:
        print("Exiting the Employee Management System. Goodbye!")
        break