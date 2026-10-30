

## 1. Problem Statement

The Retail Billing System with Multiple Discount Rules is designed to generate an itemized invoice for customers purchasing multiple products. The system calculates product costs based on quantities, applies category-specific taxes, provides discounts based on purchase thresholds, and enforces a maximum concession limit.

The program accepts product names, categories, prices, and quantities. It calculates the subtotal for each item and applies discounts according to predefined rules. It then calculates the applicable tax for each product category and generates the final bill.

The system also validates user inputs, prevents invalid quantities and prices, and displays an itemized invoice containing product details, discounts, taxes, and the final amount payable.

8. Display the final amount payable.



## 2. Algorithm

**Step 1:** Start the program.

**Step 2:** Enter the number of products purchased.

**Step 3:** For each product, enter the product name, category, unit price, and quantity.

**Step 4:** Validate the inputs.
- Product price must not be negative.
- Quantity must be greater than zero.
- Product category must be valid.

**Step 5:** Calculate the subtotal for each product.

Subtotal = Unit Price × Quantity

**Step 6:** Calculate the total subtotal of all products.

**Step 7:** Check the discount eligibility.
- If the subtotal is ₹10,000 or more, apply a 15% discount.
- Otherwise, if the subtotal is ₹5,000 or more, apply a 10% discount.
- Otherwise, no discount is applied.

**Step 8:** Apply the maximum concession limit of ₹1,500.

**Step 9:** Distribute the discount proportionally across the products.

**Step 10:** Calculate the taxable amount for each product after discount.

**Step 11:** Apply the category-specific tax rate to each product.

**Step 12:** Calculate the total tax and final amount payable.

Final Bill = Total Subtotal − Total Discount + Total Tax

**Step 13:** Display the itemized invoice with product names, quantities, subtotals, discounts, taxes, and final amounts.

**Step 14:** Stop the program.

---

## 3. Flowchart Using 
```mermiad



flowchart TD
    A([Start]) --> B[/Enter number of products/]
    B --> C[Initialize subtotal and invoice]
    C --> D[/Enter product name, category, price and quantity/]
    D --> E{Are inputs valid?}

    E -- No --> F[/Display error message/]
    F --> Z([Stop])

    E -- Yes --> G[Calculate product subtotal]
    G --> H{Are more products available?}

    H -- Yes --> D
    H -- No --> I[Calculate total subtotal]

    I --> J{Subtotal >= 10000?}
    J -- Yes --> K[Apply 15 percent discount]
    J -- No --> L{Subtotal >= 5000?}

    L -- Yes --> M[Apply 10 percent discount]
    L -- No --> N[Discount = 0]

    K --> O[Apply maximum concession limit]
    M --> O
    N --> O

    O --> P[Distribute discount proportionally]
    P --> Q[Calculate category-specific taxes]
    Q --> R[Calculate final bill]
    R --> S[Generate itemized invoice]
    S --> T[/Display invoice and total payable/]
    T --> U([Stop])





## 5. Sample Input

```text
Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category (electronics/clothing/grocery): electronics
Enter unit price: 2000
Enter quantity: 2

Product 2
Enter product name: Shirt
Enter category (electronics/clothing/grocery): clothing
Enter unit price: 1500
Enter quantity: 2

Product 3
Enter product name: Rice
Enter category (electronics/clothing/grocery): grocery
Enter unit price: 1000
Enter quantity: 3
```

## 6. Sample Output

```text
========== ITEMIZED INVOICE ==========
Product         Subtotal    Discount       Tax       Total
Laptop           4000.00      600.00    612.00     4012.00
Shirt            3000.00      450.00    127.50     2677.50
Rice             3000.00      450.00     51.00     2601.00
==========================================================
Total Subtotal: Rs. 10000.00
Discount Rate: 15%
Total Discount: Rs. 1500.00
Maximum Concession: Rs. 1500.00
Total Tax: Rs. 790.50
Final Amount Payable: Rs. 9290.50
```

---

