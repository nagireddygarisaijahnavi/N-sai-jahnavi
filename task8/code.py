

registrations = [
    ("Jahnavi", ("Python", "AI", "Python")),
    ("Bhavya", ("Python", "AI")),
    ("Girija", ("AI", "ML_Lab")),
    ("Samuel", ()),
    ("Banu", ("Python", "DBMS"))
]

print("COURSE REGISTRATION VALIDATION")
print("-" * 40)

for student, courses in registrations:
    errors = []

    # Check for duplicate courses
    if len(courses) != len(set(courses)):
        errors.append("Duplicate course registration")

    # Check whether any course is selected
    if len(courses) == 0:
        errors.append("No courses selected")

    # Check invalid course combination
    if "AI" in courses and "ML_Lab" in courses:
        errors.append("Invalid combination: AI and ML_Lab")

    # Display result
    if errors:
        print("\nStudent:", student)
        for error in errors:
            print("Status: INVALID -", error)
    else:
        print("\nStudent:", student)
        print("Status: VALID")
        print("Registered courses:", courses)

print("\nValidation completed.")
