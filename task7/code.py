

try:
    print("CAMPUS EVENT FINANCIAL PLANNING")

    # Step 1: Input fixed expenses
    venue = float(input("Enter venue cost: Rs. "))
    equipment = float(input("Enter equipment cost: Rs. "))
    transport = float(input("Enter transport cost: Rs. "))

    # Step 2: Input variable expenses
    catering_per_person = float(
        input("Enter catering cost per person: Rs. ")
    )
    certificate_per_person = float(
        input("Enter certificate cost per person: Rs. ")
    )

    # Step 3: Input participants and funding
    participants = int(input("Enter expected participants: "))
    sponsorship = float(input("Enter sponsorship amount: Rs. "))
    contribution = float(
        input("Enter contribution per participant: Rs. ")
    )

    # Step 4: Validate inputs
    if (
        venue < 0
        or equipment < 0
        or transport < 0
        or catering_per_person < 0
        or certificate_per_person < 0
        or participants <= 0
        or sponsorship < 0
        or contribution < 0
    ):
        print("Error: Invalid input values.")

    else:
        # Step 5: Calculate fixed expenses
        fixed_cost = venue + equipment + transport

        # Step 6: Calculate variable expenses
        variable_per_person = (
            catering_per_person + certificate_per_person
        )

        variable_cost = variable_per_person * participants

        # Step 7: Calculate total budget
        total_budget = fixed_cost + variable_cost

        # Step 8: Calculate sponsorship shortfall
        shortfall = max(0, total_budget - sponsorship)

        # Step 9: Calculate participant contributions
        total_contributions = contribution * participants

        # Step 10: Calculate total available funds
        total_funds = sponsorship + total_contributions

        # Step 11: Calculate remaining funding gap
        funding_gap = max(0, total_budget - total_funds)

        # Step 12: Calculate break-even registrations
        net_contribution = contribution - variable_per_person

        if sponsorship >= fixed_cost:
            break_even = 0

        elif net_contribution > 0:
            break_even = math.ceil(
                (fixed_cost - sponsorship) / net_contribution
            )

        else:
            break_even = None

        # Step 13: Display financial report
        print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")

        print(f"Venue Cost: Rs. {venue:.2f}")
        print(f"Equipment Cost: Rs. {equipment:.2f}")
        print(f"Transport Cost: Rs. {transport:.2f}")

        print(f"Fixed Expenses: Rs. {fixed_cost:.2f}")
        print(f"Variable Expenses: Rs. {variable_cost:.2f}")
        print(f"Total Event Budget: Rs. {total_budget:.2f}")

        print(f"Sponsorship: Rs. {sponsorship:.2f}")
        print(f"Funding Shortfall Before Contributions: "
              f"Rs. {shortfall:.2f}")

        print(f"Expected Participants: {participants}")
        print(f"Contribution Per Participant: "
              f"Rs. {contribution:.2f}")

        print(f"Total Participant Contributions: "
              f"Rs. {total_contributions:.2f}")

        print(f"Total Available Funds: Rs. {total_funds:.2f}")
        print(f"Remaining Funding Gap: Rs. {funding_gap:.2f}")

        if break_even is None:
            print("Break-even: Not possible with current pricing.")
        else:
            print(f"Minimum Registrations to Break Even: "
                  f"{break_even}")

        if funding_gap == 0:
            print("Status: Event budget is covered.")
        else:
            print("Status: Additional funding is required.")

except ValueError:
    print("Error: Please enter valid numeric values.")
