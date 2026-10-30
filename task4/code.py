

total_revenue = 0
total_refunds = 0
total_dispatched = 0
total_returned = 0
total_discrepancies = 0
inventory_summary = []

try:
    n = int(input("Enter number of products: "))

    if n <= 0:
        print("Invalid input! Number of products must be positive.")
        raise SystemExit

    for i in range(n):
        print(f"\n--- Product {i + 1} ---")

        name = input("Enter product name: ")
        price = float(input("Enter unit price: "))
        opening_stock = int(input("Enter opening stock: "))
        order_qty = int(input("Enter order quantity: "))
        discount_percent = float(input("Enter discount percentage: "))
        dispatched_qty = int(input("Enter dispatched quantity: "))
        returned_qty = int(input("Enter returned quantity: "))
        actual_stock = int(input("Enter actual closing stock: "))

        # Validate inputs
        if (
            price < 0
            or opening_stock < 0
            or order_qty < 0
            or dispatched_qty < 0
            or returned_qty < 0
            or actual_stock < 0
            or not 0 <= discount_percent <= 100
        ):
            print("Invalid input! Negative values are not allowed.")
            raise SystemExit

        if order_qty > opening_stock:
            print("Error: Order quantity exceeds available stock.")
            raise SystemExit

        if dispatched_qty > order_qty:
            print("Error: Dispatch cannot exceed order quantity.")
            raise SystemExit

        if returned_qty > dispatched_qty:
            print("Error: Returns cannot exceed dispatched quantity.")
            raise SystemExit

        # Calculate gross order value
        gross_value = price * dispatched_qty

        # Calculate discount
        discount = gross_value * discount_percent / 100

        # Calculate net sales after discount
        net_sales = gross_value - discount

        # Calculate refund for returned products
        discounted_unit_price = price * (
            1 - discount_percent / 100
        )
        refund = discounted_unit_price * returned_qty

        # Calculate final revenue
        revenue = net_sales - refund

        # Calculate expected closing stock
        expected_stock = (
            opening_stock - dispatched_qty + returned_qty
        )

        # Identify stock discrepancy
        discrepancy = actual_stock - expected_stock

        # Update totals
        total_revenue += revenue
        total_refunds += refund
        total_dispatched += dispatched_qty
        total_returned += returned_qty

        if discrepancy != 0:
            total_discrepancies += 1

        # Store product summary
        inventory_summary.append({
            "name": name,
            "opening": opening_stock,
            "ordered": order_qty,
            "dispatched": dispatched_qty,
            "returned": returned_qty,
            "expected": expected_stock,
            "actual": actual_stock,
            "discrepancy": discrepancy,
            "revenue": revenue,
            "refund": refund
        })

        # Display individual product results
        print("\nProduct:", name)
        print(f"Gross Order Value: Rs. {gross_value:.2f}")
        print(f"Discount: Rs. {discount:.2f}")
        print(f"Net Sales: Rs. {net_sales:.2f}")
        print(f"Refund: Rs. {refund:.2f}")
        print(f"Final Revenue: Rs. {revenue:.2f}")
        print("Expected Closing Stock:", expected_stock)
        print("Actual Closing Stock:", actual_stock)

        if discrepancy == 0:
            print("Stock Status: No Discrepancy")
        else:
            print("Stock Discrepancy:", discrepancy)

    # Final inventory summary
    print("\n===== FINAL INVENTORY SUMMARY =====")

    print(
        f"{'Product':<15}"
        f"{'Opening':>9}"
        f"{'Dispatch':>10}"
        f"{'Return':>9}"
        f"{'Expected':>10}"
        f"{'Actual':>9}"
        f"{'Difference':>12}"
    )

    for item in inventory_summary:
        print(
            f"{item['name']:<15}"
            f"{item['opening']:>9}"
            f"{item['dispatched']:>10}"
            f"{item['returned']:>9}"
            f"{item['expected']:>10}"
            f"{item['actual']:>9}"
            f"{item['discrepancy']:>12}"
        )

    print("\n===== RECONCILIATION REPORT =====")
    print(f"Total Products: {n}")
    print(f"Total Dispatched: {total_dispatched}")
    print(f"Total Returned: {total_returned}")
    print(f"Total Refunds: Rs. {total_refunds:.2f}")
    print(f"Total Revenue: Rs. {total_revenue:.2f}")
    print(f"Products with Discrepancies: {total_discrepancies}")

except ValueError:
    print("Invalid input! Please enter the correct data types.")
