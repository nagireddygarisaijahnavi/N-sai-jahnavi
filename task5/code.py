

MAX_CAPACITY = 30

print("EXAMINATION SEATING GENERATOR")

try:
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    # Validate classroom dimensions
    if rows <= 0 or cols <= 0:
        print("Error: Rows and columns must be positive.")
        raise SystemExit

    total_seats = rows * cols

    if total_seats > MAX_CAPACITY:
        print("Error: Classroom capacity exceeded!")
        print("Maximum capacity is", MAX_CAPACITY)
        raise SystemExit

    # Get reserved seat positions
    n = int(input("Enter number of reserved seats: "))

    if n < 0 or n > total_seats:
        print("Error: Invalid number of reserved seats.")
        raise SystemExit

    reserved = set()

    for i in range(n):
        print("Reserved seat", i + 1)
        r = int(input("Enter row number: "))
        c = int(input("Enter column number: "))

        if not (1 <= r <= rows and 1 <= c <= cols):
            print("Error: Invalid seat position.")
            raise SystemExit

        if (r, c) in reserved:
            print("Error: Duplicate reserved position.")
            raise SystemExit

        reserved.add((r, c))

    # Initialize counters
    available = 0
    reserved_count = 0
    blocked = 0

    print("\nEXAMINATION SEATING ARRANGEMENT")
    print("Legend: A = Available, R = Reserved, X = Blocked")

    # Nested loops to generate seats
    print("     ", end="")

    for c in range(1, cols + 1):
        print(f"C{c:<5}", end="")

    print()

    for r in range(1, rows + 1):
        print(f"R{r:<4}", end="")

        for c in range(1, cols + 1):
            seat_id = f"R{r}C{c}"

            if (r, c) in reserved:
                status = "R"
                reserved_count += 1

            elif c % 2 == 0:
                status = "X"
                blocked += 1

            else:
                status = "A"
                available += 1

            print(f"{seat_id}({status})", end=" ")

        print()

    # Display summary
    print("\n===== SEATING SUMMARY =====")
    print("Total Classroom Capacity:", total_seats)
    print("Available Seats:", available)
    print("Reserved Seats:", reserved_count)
    print("Blocked Seats:", blocked)

except ValueError:
    print("Error: Please enter valid integer values.")
