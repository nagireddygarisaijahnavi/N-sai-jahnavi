
## 1. Problem Statement

Develop a Python program to generate a **hollow diamond numerical pattern** based on a user-specified dimension.

The program should:
1. Accept the diamond size from the user.
2. Validate the input dimension and reject invalid values.
3. Generate a symmetric hollow diamond using numbers.
4. Maintain proper spacing and alignment.
5. Display an error message if the dimension is less than 1.

## 2. Flowchart 
```mermaid

flowchart TD
    A([Start]) --> B[/Enter diamond size n/]
    B --> C{Is n a positive integer?}
    C -- No --> D[Display Invalid Dimension]
    D --> K([End])
    C -- Yes --> E[Set row i = 1]
    E --> F{i <= n?}
    F -- Yes --> G[Print leading spaces]
    G --> H[Print first number]
    H --> I{Is row not first row?}
    I -- Yes --> J[Print inner spaces and second number]
    I -- No --> L[Move to next line]
    J --> L
    L --> M[Increase i]
    M --> F
    F -- No --> N[Set row i = n - 1]
    N --> O{i >= 1?}
    O -- Yes --> P[Print lower half with spaces and numbers]
    P --> Q[Decrease i]
    Q --> O
    O -- No --> R([End])
```

## 4. Sample Input

```text
Enter diamond size: 5
```

## 5. Sample Output

```text
Hollow Diamond Pattern:

    1
   2 2
  3   3
 4     4
5       5
 4     4
  3   3
   2 2
    1

```

