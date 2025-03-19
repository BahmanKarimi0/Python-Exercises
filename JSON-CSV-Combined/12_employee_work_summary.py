import json
import csv

try:
    with (open('timesheets.json', 'r', encoding='utf8') as r_jsonfile,
          open('employees.csv', 'r', encoding='utf8') as r_csvfile,
          open("employee_work_summary.csv", "w", encoding='utf8', newline="") as w_csvfile):
        timesheets = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        employees = list(reader)
        all_months = {month['date'][:7] for month in timesheets}
        if timesheets and employees:
            timesheets_hours = {}
            for timesheet in timesheets:
                if "2025" in timesheet['date']:
                    emp_id = timesheet['employee_id']
                    months = timesheet['date'][:7]
                    timesheets_hours[emp_id] = timesheets_hours.get(emp_id, {})
                    timesheets_hours[emp_id][months] = timesheets_hours[emp_id].get(months, 0) + int(
                        timesheet['hours_worked'])
            employee_work_summary = []
            for employee in employees:
                emp_id = employee['employee_id']
                hours_by_months = timesheets_hours.get(emp_id, {})
                total_hours_list = [hours_by_months.get(month, 0) for month in all_months]
                active_month = [h for h in total_hours_list if h > 0]
                monthly_average = round(sum(active_month) / len(active_month), 2) if active_month else 0
                for month in all_months:
                    total_hours = hours_by_months.get(month, 0)
                    employee_work_summary.append(
                        {'employee_id': emp_id, 'name': employee['name'], 'department': employee['department'],
                         'month': month, 'total_hours': total_hours, 'monthly_average': monthly_average})

            writer = csv.DictWriter(w_csvfile, fieldnames=['employee_id', 'name', 'department', 'month', 'total_hours',
                                                           'monthly_average'])
            writer.writeheader()
            writer.writerows(employee_work_summary)
            print("File employee_work_summary.csv created successfully")
        else:
            print("No data found in 'timesheets.json' or employees.csv")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'employee_id', 'department', 'date', or 'hours_worked' key")
except ValueError:
    print("Invalid 'hours_worked' value")
except Exception as e:
    print(f"Error: {e}")
