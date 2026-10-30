
## 1. Problem Statement

The Nested Loop Examination Seating Generator is designed to generate an examination seating arrangement using rows and columns in a classroom. The system assigns unique seat identifiers, manages reserved positions, applies alternate seating restrictions, and ensures that the seating arrangement does not exceed the fixed classroom capacity.

The program accepts the number of rows and columns, reserved seat positions, and seating restrictions. Using nested loops, it checks each seat and determines whether it should be marked as available, reserved, or blocked due to alternate seating restrictions.

Finally, the program displays the seating arrangement with row and column identifiers and provides a summary of total seats, reserved seats, blocked seats, and available seats.



## 2. Algorithm

**Step 1:** Start the program.

**Step 2:** Define the maximum classroom capacity.

**Step 3:** Accept the number of rows and columns.

**Step 4:** Validate the dimensions and ensure that the total number of seats does not exceed the classroom capacity.

**Step 5:** Accept the number of reserved seats and their row and column positions.

**Step 6:** Validate the reserved positions to ensure that they are within the classroom boundaries and do not contain duplicates.

**Step 7:** Use an outer loop to iterate through each row.

**Step 8:** Use an inner loop to iterate through each column.

**Step 9:** Generate a unique seat identifier for every position.

**Step 10:** Check the seating conditions:
- If the position is reserved, mark it as `RESERVED`.
- If the column is even-numbered, mark it as `BLOCKED`.
- Otherwise, mark it as `AVAILABLE`.

**Step 11:** Display the seating arrangement with row and column identifiers.

**Step 12:** Count the available, reserved, and blocked seats.

**Step 13:** Display the seating summary.

**Step 14:** Stop the program.

---

4 ##flowchart
```mermind
flowchart TD
    A([Start]) --> B[Set maximum classroom capacity]
    B --> C[/Enter number of rows and columns/]
    C --> D{Are dimensions valid?}
    D -- No --> E[/Display invalid dimensions/]
    E --> Z([Stop])

    D -- Yes --> F{Is total capacity within limit?}
    F -- No --> G[/Display capacity exceeded/]
    G --> Z

    F -- Yes --> H[/Enter reserved seat positions/]
    H --> I{Are reserved positions valid?}
    I -- No --> J[/Display invalid reserved positions/]
    J --> Z

    I -- Yes --> K[Initialize seat counters]
    K --> L[Select next row]
    L --> M[Select next column]
    M --> N[Generate seat identifier]
    N --> O{Is seat reserved?}

    O -- Yes --> P[Mark seat RESERVED]
    O -- No --> Q{Is column even?}

    Q -- Yes --> R[Mark seat BLOCKED]
    Q -- No --> S[Mark seat AVAILABLE]

    P --> T[Update counters]
    R --> T
    S --> T

    T --> U{More columns?}
    U -- Yes --> M
    U -- No --> V{More rows?}

    V -- Yes --> L
    V -- No --> W[Display seating arrangement]
    W --> X[Display seating summary]
    X --> Y([Stop])
```




## 5. Sample Input

```text
EXAMINATION SEATING GENERATOR
Enter number of rows: 3
Enter number of columns: 4
Enter number of reserved seats: 2

Reserved seat 1
Enter row number: 1
Enter column number: 3

Reserved seat 2
Enter row number: 2
Enter column number: 2
```

## 6. Sample Output

```text
EXAMINATION SEATING ARRANGEMENT
Legend: A = Available, R = Reserved, X = Blocked

     C1    C2    C3    C4
R1   R1C1(A) R1C2(X) R1C3(R) R1C4(X)
R2   R2C1(A) R2C2(R) R2C3(A) R2C4(X)
R3   R3C1(A) R3C2(X) R3C3(A) R3C4(X)

===== SEATING SUMMARY =====
Total Classroom Capacity: 12
Available Seats: 4
Reserved Seats: 2
Blocked Seats: 6
```

---

