import pandas as pd  # Import pandas as alias

# Load dataset 
df = pd.read_csv("train.csv")

# -----------------------------
# STEP 1: EXPLORATION
# -----------------------------

print(df.head())      # Show first 5 rows
print(df.info())      # Show column info (data types & nulls)
print(df.describe())  # Statistical summary

# -----------------------------
# STEP 2: DATA CLEANING
# -----------------------------

# Fill missing Age values with median
df["Age"].fillna(df["Age"].median(), inplace=True)  #permanent update of data

# Fill missing Embarked values with mode (most frequent value)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Drop Cabin column (too many missing values)
df.drop(columns=["Cabin"], inplace=True)

# Remove duplicate rows (if any)
df.drop_duplicates(inplace=True)

# -----------------------------
# STEP 3: DATA ANALYSIS
# -----------------------------

# Survival rate by gender
survival_by_gender = df.groupby("Sex")["Survived"].mean()
print("Survival Rate by Gender:\n", survival_by_gender)

# Survival rate by class
survival_by_class = df.groupby("Pclass")["Survived"].mean()
print("Survival Rate by Class:\n", survival_by_class)

# Average age per class
avg_age_class = df.groupby("Pclass")["Age"].mean()
print("Average Age per Class:\n", avg_age_class)

# Create age groups
df["AgeGroup"] = pd.cut(df["Age"],
                       bins=[0, 12, 18, 60, 100],
                       labels=["Child", "Teen", "Adult", "Senior"])

# Survival rate by age group
survival_by_age_group = df.groupby("AgeGroup")["Survived"].mean()
print("Survival Rate by Age Group:\n", survival_by_age_group)

# -----------------------------
# STEP 4: FILTERING
# -----------------------------

# Female passengers who survived
female_survived = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print("Female Survivors:\n", female_survived)

# Children who survived (Age < 12)
children_survived = df[(df["Age"] < 12) & (df["Survived"] == 1)]
print("Children Survivors:\n", children_survived)

# 1st class passengers with high survival (Survived = 1)
first_class_survived = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]
print("1st Class Survivors:\n", first_class_survived)

# -----------------------------
# STEP 5: INSIGHTS
# -----------------------------

print("\n--- INSIGHTS ---")

# 1. Who was more likely to survive?
print("1. Females had a higher survival rate than males.")

# 2. Did class affect survival?
print("2. Yes, 1st class passengers had significantly higher survival rates than 2nd and 3rd class.")

# 3. Were children prioritized?
print("3. Yes, children had higher survival rates compared to adults.")

# 4. Highest survival combination
print("4. The highest survival rate was among female passengers in 1st class (especially children).")
