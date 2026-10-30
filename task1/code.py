


MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 300000

eligible = []
rejected = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    sid = int(input("Student ID: "))
    name = input("Student Name: ")
    aggregate = float(input("Aggregate Marks: "))

    subjects = list(map(int, input(
        "Enter subject marks separated by spaces: "
    ).split()))

    attendance = float(input("Attendance Percentage: "))
    income = float(input("Annual Family Income: "))

    reasons = []

    # Check eligibility
    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate marks below 75%")

    if not subjects or min(subjects) < MIN_SUBJECT_MARKS:
        reasons.append("Subject marks below minimum")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income > MAX_INCOME:
        reasons.append("Family income exceeds limit")

    student = {
        "id": sid,
        "name": name,
        "aggregate": aggregate,
        "min_subject": min(subjects) if subjects else 0,
        "attendance": attendance,
        "income": income
    }

    if len(reasons) == 0:
        eligible.append(student)
    else:
        rejected.append((student, reasons))


# Sort eligible students and resolve ties
eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        -s["min_subject"],
        s["income"],
        s["id"]
    )
)

# Display eligible students
print("\n========== ELIGIBLE STUDENTS ==========")
print("Rank ID   Name     Marks   Attendance")

for rank, s in enumerate(eligible, start=1):
    print(
        rank,
        s["id"],
        s["name"],
        s["aggregate"],
        str(s["attendance"]) + "%"
    )

# Display rejected students
print("\n========== REJECTED STUDENTS ==========")

for s, reasons in rejected:
    print("\nID:", s["id"])
    print("Name:", s["name"])
    print("Reason:", ", ".join(reasons))

# Final summary
print("\n========== FINAL SUMMARY ==========")
print("Total Applicants:", n)
print("Eligible Students:", len(eligible))
print("Rejected Students:", len(rejected))
print("\nScholarship Allocation Completed!")

