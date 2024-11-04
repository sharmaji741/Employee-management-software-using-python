import pandas as pd
import matplotlib.pyplot as plt

# Welcome message
print("=====================WELCOME-SIR=============================")
print("=========WELCOME-TO-EMPLOYEE-MANAGEMENT-SOFTWARE-BASED-ON-PYTHON-PANDAS=========")
df = pd.read_csv('employees.csv')
print("=====================Employees--Data========================")
print(df)
print("=====================Which-Task-You-Want-To-Do=====================")
print("--------Main Menu with Data Manipulation---------")
print("Enter 1 to add new Employee Record")
print("Enter 2 to remove Employee Record")
print("Enter 3 to search Employee Detail BY Employee Name")
print("Enter 4 to update Employee Record")
print("----------------------------------Data Visualisation---------------------------------")
print("Enter 5 for Data Visualisation")

task = int(input("Enter Your Task: "))

# Add new Employee Record
if task == 1:
    print("NOTE: Employee ID should be a unique number.")
    employeeid = input("Enter EmployeeID: ")
    employeename = input("Enter Employee Name: ")
    department = input("Enter Employee Department: ")
    position = input("Enter Employee Position: ")
    salary = int(input("Enter Employee Salary: "))
    newemployee = pd.DataFrame({
        'EmployeeID': [employeeid],
        'EmployeeName': [employeename],
        'Department': [department],
        'Position': [position],
        'Salary': [salary]
    })
    df = pd.concat([df, newemployee], ignore_index=True)
    df.to_csv('employees.csv', index=False)
    print(df)

# Remove Employee Record
elif task == 2:
    employeeid = (input("Enter EmployeeID to remove: "))
    df = df[df['EmployeeID'] != employeeid]
    df.to_csv('employees.csv', index=False)
    print(df)

# Search Employee Detail BY Employee Name
elif task == 3:
    employeename = input("Enter Employee Name: ")
    employees_name = df[df['EmployeeName'] == employeename]
    if not employees_name.empty:
        print(employees_name)
    else:
        print("No employee found with that name.")

# Update Employee Record
elif task == 4:
    print("--------Which Field Do You Want To Update---------")
    print("Enter 1 for Employee Name")
    print("Enter 2 for Department")
    print("Enter 3 for Position")
    print("Enter 4 for Salary")
    update = int(input("Enter the Number: "))
    employeeid = (input("Enter Employee ID: "))

    if employeeid in df['EmployeeID'].values:
        if update == 1:
            name = input("Enter the new name: ")
            df.loc[df['EmployeeID'] == employeeid, 'EmployeeName'] = name
        elif update == 2:
            department = input("Enter the new department: ")
            position = input("Enter the new position: ")
            df.loc[df['EmployeeID'] == employeeid, 'Position'] = position
            df.loc[df['EmployeeID'] == employeeid, 'Department'] = department
        elif update == 3:
            position = input("Enter the new position: ")
            df.loc[df['EmployeeID'] == employeeid, 'Position'] = position
        elif update == 4:
            salary = int(input("Enter the new salary: "))
            df.loc[df['EmployeeID'] == employeeid, 'Salary'] = salary
        df.to_csv('employees.csv', index=False)
        print(df)
    else:
        print("Employee ID not found.")

# Data Visualization
elif task == 5:
    print("Enter 1 for Line Graph")
    print("Enter 2 for Bar Graph")
    graph = int(input("Choose graph type (1 or 2): "))

    if graph == 1:
        print("Enter 1 for Relation Between Salary And EmployeeName")
        print("Enter 2 for Relation Between Salary And Department")
        print("Enter 3 for Relation Between Salary And Position")
        line = int(input("Choose relation type: "))

        if line == 1:
            plt.plot(df['EmployeeName'], df['Salary'], color='g')
            plt.xlabel("Employee Name")
            plt.ylabel("Salary")
            plt.title("Relation Between Salary And EmployeeName")
            plt.show()
        elif line == 2:
            plt.plot(df['Department'], df['Salary'], color='g')
            plt.xlabel("Department")
            plt.ylabel("Salary")
            plt.title("Relation Between Salary And Department")
            plt.show()
        elif line == 3:
            plt.plot(df['Position'], df['Salary'], color='g')
            plt.xlabel("Position")
            plt.ylabel("Salary")
            plt.title("Relation Between Salary And Position")
            plt.show()

    elif graph == 2:
        print("Enter 1 for Relation Between Salary And EmployeeName")
        print("Enter 2 for Relation Between Salary And Department")
        print("Enter 3 for Relation Between Salary And Position")
        bar = int(input("Choose relation type: "))

        if bar == 1:
            plt.bar(df['EmployeeName'], df['Salary'], color='b')
            plt.xlabel("Employee Name")
            plt.ylabel("Salary")
            plt.title("Relation Between Salary And EmployeeName")
            plt.show()
        elif bar == 2:
            plt.bar(df['Department'], df['Salary'], color='b')
            plt.xlabel("Department")
            plt.ylabel("Salary")
            plt.title("Relation Between Salary And Department")
            plt.show()
        elif bar == 3:
            plt.bar(df['Position'], df['Salary'], color='b')
            plt.xlabel("Position")
            plt.ylabel("Salary")
            plt.title("Relation Between Salary And Position")
            plt.show()
