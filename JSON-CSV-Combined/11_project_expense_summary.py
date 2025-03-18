import json
import csv

try:
    with (open("expenses.json", "r", encoding="utf-8") as r_jsonfile,
          open("projects.csv", "r", encoding="utf-8") as r_csvfile,
          open("project_expense_summary.csv", "w", encoding="utf-8", newline="") as w_csvfile):
        read_data = json.load(r_jsonfile)
        reader = csv.DictReader(r_csvfile)
        projects = list(reader)
        if read_data and projects:
            categories = {}
            all_category = set(expense['category'] for expense in read_data)
            for category in read_data:
                categories[category['project_id']] = categories.get(category['project_id'], {})
                categories[category['project_id']][category['category']] = categories[category['project_id']].get(
                    category['category'], 0) + float(category['amount'])
                for expense in all_category:
                    if expense not in categories[category['project_id']]:
                        categories[category['project_id']][expense] = categories[category['project_id']].get(expense, 0)
            project_expense = []
            for project in projects:
                if project['project_id'] not in categories:
                    categories[project['project_id']] = {}
                for expense in all_category:
                    categories[project['project_id']][expense] = categories[project['project_id']].get(expense, 0)
                    total_amount = categories[project['project_id']].get(expense, 0)
                    percentage = round((float(total_amount) / float(project['budget'])) * 100, 2) if float(project[
                                                                                                               'budget']) > 0 else 0
                    project_expense.append(
                        {'project_id': project['project_id'], 'name': project['name'], 'budget': project['budget'],
                         'category': expense, 'total_amount': total_amount,
                         'percentage': percentage})
            writer = csv.DictWriter(w_csvfile,
                                    fieldnames=['project_id', 'name', 'budget', 'category', 'total_amount',
                                                'percentage'])
            writer.writeheader()
            writer.writerows(project_expense)
            print("File project_expense_summary.csv created successfully")
        else:
            print("No data found in projects.csv or expenses.json")
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except json.JSONDecodeError:
    print("JSON decode error")
except KeyError:
    print("Missing 'project_id', 'category', or 'amount' key")
except ValueError:
    print("Invalid 'amount' or 'budget' value")
except Exception as e:
    print(f"Error: {e}")
