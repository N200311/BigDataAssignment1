import pandas as pd
import sys
import subprocess

def data_processing(file_path, next_script="eda.py"):
    try:
        df = pd.read_csv(file_path)

        # Data Cleaning
        df['Age'].fillna(df['Age'].median(), inplace=True)  # Fill missing ages with median
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Fill missing embarked with mode
        df.drop(columns=['Cabin'], inplace=True)  # Drop Cabin due to many missing values

        # Data Transformation
        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})  # Encode gender
        df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

        # Data Reduction
        df.drop(columns=['Name', 'Ticket'], inplace=True)  # Drop non-essential columns
        df = df[df['Fare'] < 300]  # Remove outliers for Fare

        # Data Discretization
        df['Fare'] = pd.cut(df['Fare'], bins=4, labels=["Low", "Medium", "High", "Very High"])
        df['Age'] = pd.cut(df['Age'], bins=4, labels=["Child", "Young Adult", "Adult", "Senior"])

        df.to_csv("res_dpre.csv", index=False)
        subprocess.run(["python3", next_script, "res_dpre.csv"])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dpre.py <file_path>")
    else:
        data_processing(sys.argv[1])
