source code



# Step 1: Get hospital charges
consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Step 2: Validate charges
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input! Charges cannot be negative.")

else:
    # Step 3: Calculate total bill
    total_bill = consultation + diagnostic + treatment

    # Step 4: Check concession eligibility
    eligibility = input("Is the patient eligible for concession? (yes/no): ").lower()

    if eligibility == "yes":
        discount = total_bill * 0.10
    elif eligibility == "no":
        discount = 0
    else:
        print("Invalid concession eligibility.")
        exit()

    # Step 5: Calculate final bill
    final_bill = total_bill - discount

    # Step 6: Accept payment
    amount_paid = float(input("Enter amount paid: "))

    # Step 7: Validate payment
    if amount_paid < 0 or amount_paid > final_bill:
        print("Invalid payment amount.")

    else:
        # Step 8: Calculate remaining balance
        balance = final_bill - amount_paid

        # Step 9: Classify patient
        if balance == 0:
            classification = "Full Payment Patient"
        elif amount_paid > 0:
            classification = "Partial Payment Patient"
        else:
            classification = "Pending Payment Patient"

        # Step 10: Display bill details
        print("\n--- HOSPITAL BILL DETAILS ---")
        print(f"Consultation Charges: Rs. {consultation:.2f}")
        print(f"Diagnostic Charges: Rs. {diagnostic:.2f}")
        print(f"Treatment Charges: Rs. {treatment:.2f}")
        print(f"Total Bill: Rs. {total_bill:.2f}")
        print(f"Concession: Rs. {discount:.2f}")
        print(f"Final Bill: Rs. {final_bill:.2f}")
        print(f"Amount Paid: Rs. {amount_paid:.2f}")
        print(f"Remaining Balance: Rs. {balance:.2f}")
        print(f"Patient Classification: {classification}")
