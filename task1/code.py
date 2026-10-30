

# Category-wise GST rates
tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "groceries": 0
}

# Discount rules
MAX_DISCOUNT = 2000

products = []
total_subtotal = 0
total_tax = 0

# Input number of products
n = int(input("Enter number of products: "))

# Read product details
for i in range(n):
    print("\nEnter details of Product", i + 1)

    pid = input("Product ID: ")
    name = input("Product Name: ")
    category = input("Category (electronics/clothing/groceries): ").lower()
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    if category not in tax_rates:
        print("Invalid category! Please enter a valid category.")
        continue

    # Calculate subtotal
    subtotal = price * quantity

    # Calculate category-specific tax
    tax = subtotal * tax_rates[category] / 100

    # Store product details
    products.append({
        "id": pid,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
        "tax": tax
    })

    total_subtotal += subtotal
    total_tax += tax

# Calculate amount before discount
total_amount = total_subtotal + total_tax

# Apply threshold-based discount
if total_amount > 10000:
    discount_rate = 10
elif total_amount > 5000:
    discount_rate = 5
else:
    discount_rate = 0

discount = total_amount * discount_rate / 100

# Apply maximum concession limit
discount = min(discount, MAX_DISCOUNT)

# Calculate final amount
final_amount = total_amount - discount

# Generate invoice
print("\n" + "=" * 65)
print("                 RETAIL BILLING INVOICE")
print("=" * 65)

print(f"{'ID':<8}{'Product':<15}{'Qty':<6}{'Price':<10}{'Subtotal':<12}{'Tax':<10}")
print("-" * 65)

for p in products:
    print(
        f"{p['id']:<8}{p['name']:<15}"
        f"{p['quantity']:<6}{p['price']:<10.2f}"
        f"{p['subtotal']:<12.2f}{p['tax']:<10.2f}"
    )

print("-" * 65)

print(f"Subtotal Amount       : Rs. {total_subtotal:.2f}")
print(f"Total GST             : Rs. {total_tax:.2f}")
print(f"Amount Before Discount: Rs. {total_amount:.2f}")
print(f"Discount Rate         : {discount_rate}%")
print(f"Discount Amount       : Rs. {discount:.2f}")
print(f"Maximum Concession    : Rs. {MAX_DISCOUNT:.2f}")
print("-" * 65)
print(f"FINAL PAYABLE AMOUNT  : Rs. {final_amount:.2f}")
print("=" * 65)
print("          THANK YOU! VISIT AGAIN!")


