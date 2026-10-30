

budget = 50000

# Exchange rates: 1 unit of foreign currency in INR
exchange_rates = {
    "USD": 85.0,
    "EUR": 92.0,
    "GBP": 110.0
}

conversion_fee_percent = 2

# Travel expenses: category, amount, currency
expenses = [
    ("Hotel", 200, "USD"),
    ("Food", 100, "EUR"),
    ("Transport", 50, "GBP"),
    ("Shopping", 150, "USD")
]

total_expenses = 0
category_totals = {}

print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
print("-" * 45)

for category, amount, currency in expenses:
    if currency not in exchange_rates:
        print("Invalid currency:", currency)
        continue

    # Convert expense into INR
    converted_amount = amount * exchange_rates[currency]

    # Calculate conversion fee
    fee = converted_amount * conversion_fee_percent / 100

    # Total expense including fee
    final_amount = converted_amount + fee

    # Store category expense
    category_totals[category] = final_amount
    total_expenses += final_amount

    print("\nCategory:", category)
    print("Original Amount:", amount, currency)
    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Amount: Rs.", round(final_amount, 2))

# Find largest expense category
largest_category = max(category_totals, key=category_totals.get)

print("\n" + "-" * 45)
print("Travel Budget: Rs.", budget)
print("Total Expenses: Rs.", round(total_expenses, 2))

# Compare expenses with budget
if total_expenses > budget:
    print("Budget Status: EXCEEDED")
    print("Amount Exceeded: Rs.",
          round(total_expenses - budget, 2))
else:
    print("Budget Status: WITHIN BUDGET")
    print("Remaining Budget: Rs.",
          round(budget - total_expenses, 2))

print("Largest Expense Category:", largest_category)
print("Largest Category Amount: Rs.",
      round(category_totals[largest_category], 2))

print("\nAnalysis Completed.")
