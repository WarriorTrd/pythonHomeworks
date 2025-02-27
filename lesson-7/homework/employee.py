class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class EmployeeManager:
    file = "employees.txt"
    
    def __init__(self):
        try:
            with open(self.file, "r") as file:
                pass
        except FileNotFoundError:
            with open(self.file, "w") as file:
                pass
    
    def add_employee(self, employee):
        if self.get_employee(employee.employee_id):
            print("Employee ID already exists!")
            return
        with open(self.file, "a") as file:
            file.write(f"{employee}\n")
        print("Employee added successfully!")
    
    def view_all_employees(self):
        with open(self.file, "r") as file:
            records = file.readlines()
        if not records:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for record in records:
                print(record.strip())
    
    def get_employee(self, employee_id):
        with open(self.file, "r") as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == employee_id:
                    return Employee(*data)
        return None
    
    def update_employee(self, employee_id, name, position, salary):
        employees = []
        updated = False
        with open(self.file, "r") as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == employee_id:
                    employees.append(f"{employee_id}, {name}, {position}, {salary}\n")
                    updated = True
                else:
                    employees.append(line)
        if updated:
            with open(self.file, "w") as file:
                file.writelines(employees)
            print("Employee updated successfully!")
        else:
            print("Employee not found.")
    
    def delete_employee(self, employee_id):
        employees = []
        deleted = False
        with open(self.file, "r") as file:
            for line in file:
                data = line.strip().split(", ")
                if data[0] == employee_id:
                    deleted = True
                else:
                    employees.append(line)
        if deleted:
            with open(self.file, "w") as file:
                file.writelines(employees)
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")
    
    def sort_employees(self, sort_by):
        with open(self.file, "r") as file:
            records = [line.strip().split(", ") for line in file]
        if sort_by == "name":
            records.sort(key=lambda x: x[1].lower())
        elif sort_by == "salary":
            records.sort(key=lambda x: int(x[3]))
        for record in records:
            print(", ".join(record))

def main():
    manager = EmployeeManager()
    while True:
        choice = input("""
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Sort employees
7. Exit
Enter your choice: """)
        
        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            manager.add_employee(Employee(emp_id, name, position, salary))
        elif choice == "2":
            manager.view_all_employees()
        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            employee = manager.get_employee(emp_id)
            print(employee if employee else "Employee not found.")
        elif choice == "4":
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name: ")
            position = input("Enter new Position: ")
            salary = input("Enter new Salary: ")
            manager.update_employee(emp_id, name, position, salary)
        elif choice == "5":
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)
        elif choice == "6":
            sort_by = input("Sort by name or salary? ")
            if sort_by in ["name", "salary"]:
                manager.sort_employees(sort_by)
            else:
                print("Invalid sort option.")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
