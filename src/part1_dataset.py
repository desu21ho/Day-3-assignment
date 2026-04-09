import pandas as pd  # Import pandas library using alias method

# Create a dictionary of employee with (5 columns: Name, age, city,salary and profession; 15 rows)
data = {
    "Name": [
        "Abel", "Sara", "Dawit", "Meklit", "Tesfaye",
        "Hana", "Yonas", "Selam", "Biruk", "Rahel",
        "Kebede", "Liya", "Samuel", "Almaz", "Henok"
    ],
    "Age": [
        23, 21, 25, 22, 30,
        19, 28, 24, 27, 26,
        35, 20, 29, 32, 31
    ],
    "City": [
        "Addis Ababa", "Hawassa", "Bahir Dar", "Mekelle", "Jimma",
        "Dire Dawa", "Adama", "Gondar", "Harar", "Jimma",
        "Addis Ababa", "Hawassa", "Bahir Dar", "Mekelle", "Adama"
    ],
    "Salary_ETB": [
        12000, 10000, 15000, 11000, 18000,
        9000, 16000, 13000, 14000, 12500,
        20000, 9500, 17000, 19000, 17500
    ],
    "Profession": [
        "Engineer", "Student", "Teacher", "Designer", "Manager",
        "Student", "Doctor", "Engineer", "Lawyer", "Teacher",
        "Manager", "Student", "Doctor", "Manager", "Engineer"
    ]
}

# Custom index (15 unique labels) as employee(E) folowwed by 1 to 15 numbers
index_labels = [
    "E01", "E02", "E03", "E04", "E05",
    "E06", "E07", "E08", "E09", "E10",
    "E11", "E12", "E13", "E14", "E15"
]

# Create DataFrame
df_employee = pd.DataFrame(data, index=index_labels)

# Display dataset
print(df_employee)
