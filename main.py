from expense import Expense
from file_manager import initialize_csv, save_expense, load_expenses, backup_data
from report import category_summary, monthly_report, search_expenses

initialize_csv()
expenses = load_expenses()

def add_expense():
    print("\nADD NEW EXPENSE:")
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food/Transport/Entertainment/Shopping/Other): ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        expense = Expense(amount, category, date, description)
        expenses.append(expense)
        save_expense(expense)

        print("\n Expense added successfully!")
    except ValueError:
        print("\n Invalid amount!")

def view_all_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return
    print("\nALL EXPENSES:")
    for e in expenses:
        print(f"{e.date} | ₹{e.amount} | {e.category} | {e.description}")

def view_category_summary():
    print("\nCATEGORY-WISE SUMMARY:")
    summary = category_summary(expenses)
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt}")

def generate_monthly_report():
    month = input("\nEnter month (YYYY-MM): ")
    total = monthly_report(expenses, month)
    print(f"Total expenses for {month}: ₹{total}")

def search_menu():
    keyword = input("\nEnter keyword: ")
    results = search_expenses(expenses, keyword)
    for e in results:
        print(f"{e.date} | ₹{e.amount} | {e.category} | {e.description}")

def main():
    while True:
        print("\n==========================================")
        print("     PERSONAL FINANCE MANAGER")
        print("==========================================")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. View Category-wise Summary")
        print("4. Generate Monthly Report")
        print("5. Search Expenses")
        print("6. Backup Data")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_category_summary()
        elif choice == "4":
            generate_monthly_report()
        elif choice == "5":
            search_menu()
        elif choice == "6":
            backup_data()
            print("\nBackup completed!")
        elif choice == "7":
            print("\nThank you for using Personal Finance Manager 👋")
            break
        else:
            print("\n Invalid choice")

        input("\nPress Enter to continue...")

main()
