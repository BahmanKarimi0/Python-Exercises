import json
import csv

try:
    with (open("tasks.json", "r", encoding="utf-8") as r_jsonfile,
          open("employees.csv", "r", encoding="utf-8") as r_csvfile,
          open("completed_hours.csv", "w", encoding="utf-8", newline="") as w_csvfile):
        read_data = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        employees = list(reader)
        if read_data and employees:
            completed_tasks_hours = {}
            for task in read_data:
                if task['status'] == "completed":
                    completed_tasks_hours[task['employee_id']] = completed_tasks_hours.get(task['employee_id'],
                                                                                           0) + int(
                        task['hours'])
                elif task['employee_id'] not in completed_tasks_hours:
                    completed_tasks_hours[task['employee_id']] = 0

            completed_hours = []
            for employee in employees:
                total_hours = completed_tasks_hours.get(employee['employee_id'], 0)
                completed_hours.append(
                        {'employee_id': employee['employee_id'], 'name': employee['name'],
                         'department': employee['department'],
                         'total_hours': total_hours})

            writer = csv.DictWriter(w_csvfile, fieldnames=['employee_id', 'name', 'department', 'total_hours'])
            writer.writeheader()
            writer.writerows(completed_hours)
            print("File completed_hours.csv created successfully")
        else:
            print("No data available in 'employees.csv' or 'tasks.json'")
except FileNotFoundError:
    print("No data available in 'employees.csv' or 'tasks.json'")
except PermissionError:
    print("Permission denied")
except KeyError:
    print("Missing 'employee_id' or 'hours' or 'status' key")
except json.JSONDecodeError:
    print("JSON decoding error")
except ValueError:
    print("Invalid 'employee_id' or 'hours' or 'status' value")
except Exception as e:
    print(f"Error: {e}")
