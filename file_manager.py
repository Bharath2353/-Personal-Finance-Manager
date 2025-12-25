import csv
import os
from expense import Expense

FILE_NAME = "expenses.csv"
BACKUP_FILE = "backup.csv"

def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Amount", "Category", "Date", "Description"])

def save_expense(expense):
    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(expense.to_list())

def load_expenses():
    expenses = []
    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(
                Expense(
                    float(row["Amount"]),
                    row["Category"],
                    row["Date"],
                    row["Description"]
                )
            )
    return expenses

def backup_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as src, open(BACKUP_FILE, "w", newline="") as dest:
            dest.write(src.read())
