import pandas as pd
import sys
import subprocess

def eda(file_path, next_script="vis.py"):
    try:
        df = pd.read_csv(file_path)

        # Insights
        total_passengers = f"Total passengers: {df.shape[0]}"
        survival_rate = f"Survival rate: {df['Survived'].mean() * 100:.2f}%"
        gender_survival = f"Female survival rate: {df[df['Sex'] == 1]['Survived'].mean() * 100:.2f}%, Male survival rate: {df[df['Sex'] == 0]['Survived'].mean() * 100:.2f}%"

        insights = [total_passengers, survival_rate, gender_survival]

        for i, insight in enumerate(insights):
            with open(f"eda-in-{i+1}.txt", "w") as f:
                f.write(insight)

        subprocess.run(["python3", next_script, file_path])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 eda.py <file_path>")
    else:
        eda(sys.argv[1])
