# 1.create a dictionary with following fields:
# name:employee
# id,name,role,basic,hra,da
# insert five fields data
# find total salary
# create a  text file insert dictionary in text format

employees = {
    1: {"name": "John", "role": "Manager", "basic": 5000, "hra": 1000, "da": 500},
    2: {"name": "Alice", "role": "Developer", "basic": 6000, "hra": 1200, "da": 600},
    3: {"name": "Bob", "role": "Designer", "basic": 5500, "hra": 1100, "da": 550},
    4: {"name": "Charlie", "role": "Tester", "basic": 4800, "hra": 900, "da": 480},
    5: {"name": "Eve", "role": "Support", "basic": 4500, "hra": 850, "da": 450},
}


def employee_operations():

    for emp_id, data in employees.items():
        data['total_salary'] = data['basic'] + data['hra'] + data['da']

    with open("employees.txt", "w") as f:
        for emp_id, data in employees.items():
            f.write(f"ID: {emp_id}\n")
            for key, value in data.items():
                f.write(f"{key.capitalize()}: {value}\n")
            f.write("\n")


employee_operations()
