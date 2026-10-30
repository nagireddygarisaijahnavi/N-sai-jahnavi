

print("SMART PARKING FEE MANAGEMENT SYSTEM")
print("1. Two-wheeler - Rs. 10/hour")
print("2. Car - Rs. 20/hour")
print("3. Heavy vehicle - Rs. 30/hour")

vehicle = input("Enter vehicle category (two-wheeler/car/heavy): ").lower()

# Assign hourly rate
rates = {
    "two-wheeler": 10,
    "car": 20,
    "heavy": 30
}

if vehicle not in rates:
    print("Invalid vehicle category.")

else:
    try:
        # Input format: YYYY-MM-DD HH:MM
        entry_input = input(
            "Enter entry date and time (YYYY-MM-DD HH:MM): "
        )
        exit_input = input(
            "Enter exit date and time (YYYY-MM-DD HH:MM): "
        )

        entry_time = datetime.strptime(
            entry_input, "%Y-%m-%d %H:%M"
        )
        exit_time = datetime.strptime(
            exit_input, "%Y-%m-%d %H:%M"
        )

        # Validate time inputs
        if exit_time <= entry_time:
            print("Invalid input! Exit must be after entry.")

        else:
            # Calculate duration
            duration = exit_time - entry_time
            total_minutes = duration.total_seconds() / 60
            total_hours = total_minutes / 60

            # Charge every started hour, minimum one hour
            billable_hours = max(1, math.ceil(total_hours))

            hourly_rate = rates[vehicle]

            # Calculate basic parking fee
            basic_fee = billable_hours * hourly_rate

            # Calculate number of calendar days touched
            calendar_days = (
                (exit_time.date() - entry_time.date()).days + 1
            )

            # Daily limit: Rs. 200 per calendar day
            daily_limit = 200 * calendar_days
            parking_fee = min(basic_fee, daily_limit)

            # Overnight surcharge
            if exit_time.date() > entry_time.date():
                overnight_fee = 50
            else:
                overnight_fee = 0

            # Penalty for parking longer than 24 hours
            if duration > timedelta(hours=24):
                penalty = 100
            else:
                penalty = 0

            # Calculate final amount
            total_fee = parking_fee + overnight_fee + penalty

            # Display bill
            print("\n----- PARKING BILL -----")
            print("Vehicle Category:", vehicle)
            print("Entry Time:", entry_time)
            print("Exit Time:", exit_time)
            print("Parking Duration:", duration)
            print("Billable Hours:", billable_hours)
            print("Hourly Rate: Rs.", hourly_rate)
            print("Basic Parking Fee: Rs.", basic_fee)
            print("Parking Fee After Daily Limit: Rs.", parking_fee)
            print("Overnight Surcharge: Rs.", overnight_fee)
            print("Penalty: Rs.", penalty)
            print("Total Parking Fee: Rs.", total_fee)

    except ValueError:
        print("Invalid date or time format.")
        print("Use YYYY-MM-DD HH:MM.")
