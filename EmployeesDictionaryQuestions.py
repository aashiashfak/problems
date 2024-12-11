employees = {
    "101": {"name": "Alice", "designation": "Developer", "salary": 50000},
    "102": {"name": "Bob", "designation": "Designer", "salary": 45000},
    "103": {"name": "Charlie", "designation": "Manager", "salary": 60000},
}

employees["104"] = {"name": "David", "designation": "Tester", "salary": 55000}
employees.pop("101")

def set_employees_designation(employees):
    for employee_id, employee_info in employees.items():
        if employee_id == '102':
            employee_info['designation'] = 'Senior Designer'
        else:
            continue
    return employees

set_employees_designation(employees)


def increase_salary_10(employees):
    for employee_id, employee_info in employees.items():
        salary = employee_info['salary'] * 1.10  
        employee_info['salary'] = int(salary)
    return employees


increase_salary_10(employees)

for employee_id,employee_info in employees.items():
    print(employee_id , employee_info,  end="\n")