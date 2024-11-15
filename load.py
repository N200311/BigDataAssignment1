import pandas as pd
import sys
import subprocess

def load_dataset(file_path, next_script="dpre.py"):
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully! Shape: {df.shape}")
        df.to_csv("temp_load.csv", index=False)  # Save intermediate data
        subprocess.run(["python3", next_script, "temp_load.csv"])  # Invoke next script
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <file_path>")
    else:
        load_dataset(sys.argv[1])
