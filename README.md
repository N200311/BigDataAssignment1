﻿# Big Data assignment1 README

github repo

all commands:

mkdir bd-a1
cd bd-a1
docker build -t doc-bd-a1 .  
docker run -it --name bd-a1-container doc-bd-a1
nano load.py dpre.py eda.py vis.py model.py final.sh
python3 load.py TitanicDataset.csv
bash final.sh

This is a README file showing the execution of the project, including all Docker commands used:

---

# Big Data Assignment 1 - README

## Introduction
This project aims to demonstrate a pipeline for Big Data analysis using Docker containers. The pipeline includes data loading, preprocessing, exploratory data analysis (EDA), visualization, and model implementation.

### Dataset
The dataset used in this project is the famous Titanic dataset.

## Setup

1. **Clone Repository**: Clone this repository to your local machine:
    ```bash
    git clone <repository_url>
    ```

2. **Download Dataset**: Download the dataset and place it in the `bd-a1/` directory.

3. **Build Docker Image**: Navigate to the `bd-a1/` directory and build the Docker image using the provided Dockerfile:
    ```bash
    cd bd-a1/
    docker build -t doc-bd-a1 .
    ```

4. **Run Docker Container**: Run the Docker container using the built image:
    ```bash
    docker run -it --name bd-a1-container doc-bd-a1
    ```

## Execution

1. **Load Data**: Inside the container, run the `load.py` script to load the dataset, this script will start the pipeline by running the other files:
    ```bash
    python3 load.py <dataset-path>
    ```
    Replace `<dataset-path>` with the path to the dataset within the container.

2. **Data Preprocessing**: Execute the data preprocessing script `dpre.py`:
    This script will perform data cleaning, transformation, reduction, and discretization.

3. **Exploratory Data Analysis (EDA)**: Run the EDA script `eda.py`:
    This script will generate insights without visualizations.

4. **Visualization**: Execute the visualization script `vis.py`:
    This script will create a visualization and save it as `vis.png`.

5. **Model Implementation**: Run the model implementation script `model.py`:
    This script will implement the K-means algorithm and save cluster information in `k.txt`.

6. **Finalize**: Execute the final script `final.sh` to copy output files to the local machine and stop the container:
    ```bash
    ./final.sh
    ```

## Bonus Tasks

- **Push Files to GitHub Repo**: 
Navigate to the repository on GitHub.

Click the "Add file" button.

In the "Name" field, type the name of the folder "bd-a1".

In the "Commit message" field, type a brief description of the folder.

Click the "Commit changes" button.

## Conclusion

This README provides detailed instructions for setting up and executing the Big Data Assignment 1 pipeline using Docker containers. Follow the steps outlined above to analyze the dataset and generate relevant insights and visualizations.

