

## 1. Problem Statement

Develop a Python program to validate student course registrations using **tuples**. Each registration is represented as a tuple containing the student name and selected courses. The program should:

1. Identify duplicate course registrations.
2. Detect invalid course combinations.
3. Identify students whose course selections violate the given rules.
4. Display valid and invalid registrations with appropriate messages.


## 2. Flowchart
```mermind


flowchart TD
    A([Start]) --> B[Define student registration tuples]
    B --> C[Define course validation rules]
    C --> D[Select a student registration]
    D --> E{More registrations?}
    E -- Yes --> F[Extract student name and courses]
    F --> G{Any duplicate courses?}
    G -- Yes --> H[Report duplicate registration]
    G -- No --> I{No courses selected?}
    H --> J{AI and ML_Lab both selected?}
    I -- Yes --> K[Report invalid registration]
    I -- No --> J
    J -- Yes --> L[Report invalid course combination]
    J -- No --> M[Mark registration as valid]
    K --> N{More registrations?}
    L --> N
    M --> N
    N -- Yes --> D
    N -- No --> O[Display validation results]
    E -- No --> O
    O --> P([End])
```


## 4. Sample Input

The following registration tuples are provided in the program:

```text
("Jahnavi", ("Python", "AI", "Python"))
("Bhavya", ("Python", "AI"))
("Girija", ("AI", "ML_Lab"))
("Samuel", ())
("Banu", ("Python", "DBMS"))
```

## 5. Sample Output

```text
COURSE REGISTRATION VALIDATION
----------------------------------------

Student: Jahnavi
Status: INVALID - Duplicate course registration

Student: Bhavya
Status: VALID
Registered courses: ('Python', 'AI')

Student: Girija
Status: INVALID - Invalid combination: AI and ML_Lab

Student: Samuel
Status: INVALID - No courses selected

Student: Banu
Status: VALID
Registered courses: ('Python', 'DBMS')

Validation completed.
```

