
import csv
import sys
import os
import custom_module
from datetime import datetime


# Task 2
def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open('../csv/employees.csv', "r") as file:
            reader = csv.reader(file)
            fields = next(reader)
            employees_dict["fields"] = fields

            for row in reader:
                rows.append(row)
            employees_dict["rows"] = rows
    except Exception as e:
        print(f"An exception occurred: {type(e).__name__}")
        print(f"Exception message: {e}")
        sys.exit(1)
    return employees_dict
employees = read_employees()
print(employees)


# Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")
print(employee_id_column)


# Task 4
def first_name(row_number):
    first_name_column = column_index("first_name")
    row = employees["rows"][row_number]
    return row[first_name_column]
print(first_name(0))


# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches
print(employee_find(2))


# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches
print(employee_find_2(2))


# Task 7
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]


# Task 8
def employee_dict(row):
    fields = employees["fields"]
    employee_dict = {key: value for key, value in zip(fields, row) if key != "employee_id"}
    return employee_dict

result = employee_dict(employees["rows"][0])
print (result)


# Task 9
def all_employees_dict():
    fields = employees["fields"]
    emp_id_index = fields.index("employee_id")
    result = {row[emp_id_index]: employee_dict(row) for row in employees["rows"]}
    return result


# Task 10
def get_this_value():
    return os.getenv("THISVALUE")
print(get_this_value())

# Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
set_that_secret("abcabcabc")
print(custom_module.secret)


# Task 12
def read_csv(filepath):
    with open(filepath, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
    return {"fields": fields, "rows": rows}

def read_minutes():
    minutes1 = read_csv("../csv/minutes1.csv")
    minutes2 = read_csv("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


# Task 13
def create_minutes_set():
    set1 = set(tuple(row) for row in minutes1["rows"])
    set2 = set(tuple(row) for row in minutes2["rows"])

    combined_set = set1.union(set2)
    return combined_set

minutes_set = create_minutes_set()
print("Combined minutes set:", minutes_set)


# Task 14
def create_minutes_list():
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return minutes_list
minutes_list = create_minutes_list()
print(minutes_list)


# Task 15
def write_sorted_list():
    for i, (name, date) in enumerate(minutes_list):
        if isinstance(date, str):
            minutes_list[i] = (name, datetime.strptime(date, "%B %d, %Y"))

    minutes_list.sort(key=lambda x: x[1])
    converted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    with open('./minutes.csv', mode="w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)
    return converted_list
sorted_minutes_list = write_sorted_list()
print(sorted_minutes_list)