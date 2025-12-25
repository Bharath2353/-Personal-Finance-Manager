from collections import defaultdict

def category_summary(expenses):
    summary = defaultdict(float)
    for e in expenses:
        summary[e.category] += e.amount
    return summary

def monthly_report(expenses, month):
    total = 0
    for e in expenses:
        if e.date.startswith(month):
            total += e.amount
    return total

def search_expenses(expenses, keyword):
    return [e for e in expenses if keyword.lower() in e.description.lower()]
