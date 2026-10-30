

# Category-specific tax rates
tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "grocery": 2
}

MAX_DISCOUNT = 1500

try:
    n = int(input("Enter number of products: "))

    if n <= 0:
        print("Error: Number of products must be positive.")
        raise SystemExit

    products = []
    total_subtotal = 0

    # Step 1: Enter product details
    for i in range(n):
        print(f"\nProduct {i + 1}")

        name = input("Enter product name: ")
        category = input(
            "Enter category (electronics/clothing/grocery): "
        ).lower()

        price = float(input("Enter unit price: "))
        quantity = int(input("Enter quantity: "))

        # Validate inputs
        if category not in tax_rates:
            print("Error: Invalid product category.")
            raise SystemExit

        if price < 0 or quantity <= 0:
            print("Error: Invalid price or quantity.")
            raise SystemExit

        subtotal = price * quantity
        total_subtotal += subtotal

        products.append({
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity,
            "subtotal": subtotal
        })

    # Step 2: Calculate threshold discount
    if total_subtotal >= 10000:
        discount_rate = 15
    elif total_subtotal >= 5000:
        discount_rate = 10
    else:
        discount_rate = 0

    discount = total_subtotal * discount_rate / 100

    # Step 3: Apply maximum concession limit
    discount = min(discount, MAX_DISCOUNT)

    # Step 4: Calculate item discounts and taxes
    total_discount = 0
    total_tax = 0
    final_bill = 0

    print("\n========== ITEMIZED INVOICE ==========")
    print(
        f"{'Product':<12}{'Subtotal':>12}"
        f"{'Discount':>12}{'Tax':>10}{'Total':>12}"
    )

    for item in products:
        subtotal = item["subtotal"]

        # Distribute discount proportionally
        if total_subtotal > 0:
            item_discount = discount * subtotal / total_subtotal
        else:
            item_discount = 0

        taxable_amount = subtotal - item_discount

        tax_rate = tax_rates[item["category"]]
        tax = taxable_amount * tax_rate / 100

        item_total = taxable_amount + tax

        total_discount += item_discount
        total_tax += tax
        final_bill += item_total

        print(
            f"{item['name']:<12}"
            f"{subtotal:>12.2f}"
            f"{item_discount:>12.2f}"
            f"{tax:>10.2f}"
            f"{item_total:>12.2f}"
        )

    # Step 5: Display invoice summary
    print("=" * 58)
    print(f"Total Subtotal: Rs. {total_subtotal:.2f}")
    print(f"Discount Rate: {discount_rate}%")
    print(f"Total Discount: Rs. {total_discount:.2f}")
    print(f"Maximum Concession: Rs. {MAX_DISCOUNT:.2f}")
    print(f"Total Tax: Rs. {total_tax:.2f}")
    print(f"Final Amount Payable: Rs. {final_bill:.2f}")

except ValueError:
    print("Error: Please enter valid numeric values.")
