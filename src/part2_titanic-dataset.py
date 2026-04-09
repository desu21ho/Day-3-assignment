import pandas as pd

# -----------------------------
# STEP 1: Load Dataset
# -----------------------------
df = pd.read_csv("data/Titanic-Dataset.csv")  # ensure CSV is in data/

# -----------------------------
# STEP 2: Data Cleaning
# -----------------------------

# Fill missing Age with median
df["Age"].fillna(df["Age"].median(), inplace=True)

# Fill missing Embarked with mode
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Drop Cabin column (too many missing)
df.drop(columns=["Cabin"], inplace=True)

# Remove duplicates if any
df.drop_duplicates(inplace=True)

# -----------------------------
# STEP 3: Analysis
# -----------------------------

# Survival rate by gender
survival_by_gender = df.groupby("Sex")["Survived"].mean()
print("Survival Rate by Gender:\n", survival_by_gender)

# Survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
print("\nSurvival Rate by Class:\n", survival_by_class)

# Average age per class
avg_age_class = df.groupby("Pclass")["Age"].mean()
print("\nAverage Age per Class:\n", avg_age_class)

# Create Age Groups
df["AgeGroup"] = pd.cut(df["Age"], bins=[0,12,18,60,100], labels=["Child","Teen","Adult","Senior"])

# Survival rate by age group
survival_by_age_group = df.groupby("AgeGroup")["Survived"].mean()
print("\nSurvival Rate by Age Group:\n", survival_by_age_group)

# -----------------------------
# STEP 4: Filtering
# -----------------------------

# Female passengers who survived
female_survived = df[(df["Sex"]=="female") & (df["Survived"]==1)]
print("\nNumber of Female Survivors:", female_survived.shape[0])

# Children who survived
children_survived = df[(df["Age"]<12) & (df["Survived"]==1)]
print("Number of Children Survivors:", children_survived.shape[0])

# First class passengers who survived
first_class_survived = df[(df["Pclass"]==1) & (df["Survived"]==1)]
print("Number of 1st Class Survivors:", first_class_survived.shape[0])

# Female + 1st class survival rate
female_1st_survival = df[(df["Sex"]=="female") & (df["Pclass"]==1)]["Survived"].mean()

# Children + 1st class survival rate
children_1st_survival = df[(df["Age"]<12) & (df["Pclass"]==1)]["Survived"].mean()

# -----------------------------
# STEP 5: Insights (Robust)
# -----------------------------

print("\n--- INSIGHTS ---")

# 1. Gender effect
if survival_by_gender["female"] > survival_by_gender["male"]:
    print("1. Females had a higher survival rate than males.")
elif survival_by_gender["female"] < survival_by_gender["male"]:
    print("1. Males had a higher survival rate than females.")
else:
    print("1. Male and female survival rates were equal.")

# 2. Class effect
best_class = survival_by_class.idxmax()
print(f"2. {best_class}st class passengers had the highest survival rate among classes.")

# 3. Age effect
best_age_group = survival_by_age_group.idxmax()
print(f"3. {best_age_group} had the highest survival rate among age groups.")

# 4. Highest survival combination
print(f"4. The highest survival combination is female passengers in 1st class: {female_1st_survival:.2f} survival rate.")

# 5. Additional: Children survival
if survival_by_age_group["Child"] > survival_by_age_group["Adult"]:
    print("5. Children had higher survival rates than adults, indicating priority in rescue.")
else:
    print("5. Adults had equal or higher survival than children (rare in Titanic dataset).")

