import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import subprocess

def visualize(file_path, next_script="model.py"):
    try:
        df = pd.read_csv(file_path)

        # Create a survival count plot
        sns.countplot(data=df, x="Survived")
        plt.title("Survival Count")
        plt.savefig("vis.png")

        subprocess.run(["python3", next_script, file_path])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 vis.py <file_path>")
    else:
        visualize(sys.argv[1])
