

try:
    n = int(input("Enter diamond size: "))

    if n < 1:
        print("Invalid dimension! Enter a positive integer.")

    else:
        print("\nHollow Diamond Pattern:\n")

        # Upper half of the diamond
        for i in range(1, n + 1):

            # Print leading spaces
            print(" " * (n - i), end="")

            # Print first number
            print(i, end="")

            # Print inner spaces and second number
            if i > 1:
                print(" " * (2 * i - 3), end="")
                print(i, end="")

            print()

        # Lower half of the diamond
        for i in range(n - 1, 0, -1):

            # Print leading spaces
            print(" " * (n - i), end="")

            # Print first number
            print(i, end="")

            # Print inner spaces and second number
            if i > 1:
                print(" " * (2 * i - 3), end="")
                print(i, end="")

            print()

except ValueError:
    print("Invalid input! Please enter an integer.")
