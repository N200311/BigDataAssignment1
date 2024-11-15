import pandas as pd
from sklearn.cluster import KMeans
import sys

def apply_kmeans(file_path):
    try:
        df = pd.read_csv(file_path)
        features = df[['Pclass', 'Age', 'Fare']].dropna()  # Suitable columns
        features_encoded = pd.get_dummies(features, drop_first=True)

        kmeans = KMeans(n_clusters=3, random_state=42)
        clusters = kmeans.fit_predict(features_encoded)

        cluster_counts = pd.Series(clusters).value_counts().to_dict()
        with open("k.txt", "w") as f:
            f.write(str(cluster_counts))

        print("Cluster counts saved as k.txt")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 model.py <file_path>")
    else:
        apply_kmeans(sys.argv[1])
