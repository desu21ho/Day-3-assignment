# Day-3-assignment
**Data Handling with Pandas Daily Assignment**

## 📌 Overview
This project demonstrates **data analysis using pandas**.  
It includes:
- Creating **a dataset** (Part 1)
- Cleaning and analyzing the **Titanic dataset** (Part 2)
- Computing **survival rates by gender, class, and age**
- Filtering passengers by gender, class, and children
- Extracting **insights directly from data**

---

## 📁 Project Structure
Day-3-assignment/
│
├── data/
│ └── Titanic-Dataset.csv
│
├── src/
│ ├── part1_dataset.py
│ ├── part2_titanic-dataset.py
│ 
│
├── main.py
├── README.md

**Tasks Completed**
✅ **Part 1: Creating Dataset**
      Created dataset with 5 features, 15 rows, and custom index
✅ **Part 2: Titanic Dataset**
      Data exploration: .head(), .info(), .describe()
      Data cleaning:
        Filled missing Age (median)
        Filled Embarked (mode)
        Dropped Cabin
        Removed duplicates
      Data analysis:
        Survival rate by gender
        Survival rate by class
        Average age per class
        Survival rate by age group
      Filtering:
        Female survivors
        Children survivors
        1st class survivors
📌 **Insights (Computed from Data)**
     Gender survival comparison: **Females had a higher survival rate than males**
     Class survival comparison: **1st class passengers had higher survival than 2nd and 3rd class**
     Age group survival comparison: **Children had higher survival rates than adult**
     Highest survival combination: **(female + 1st class): The highest survival rate was among female passengers in 1st class**
     Children survival priority
