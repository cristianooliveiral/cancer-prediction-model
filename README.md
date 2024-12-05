# Cancer Prediction Model

This project aims to develop a predictive model for cancer diagnosis based on data from **The Cancer Genome Atlas (TCGA)**. 

## Objective

The goal of this work is to create a predictive model capable of identifying the presence of cancer in patients using genomic data provided by the TCGA.

## Repository Structure

- `data/`: Contains raw and processed TCGA data.
- `notebooks/`: Jupyter notebooks for data exploration and model development.
- `src/`: Source code for preprocessing, model training, and evaluation.
- `models/`: Trained models and corresponding evaluation metrics.
- `requirements.txt`: Project dependencies.
- `README.md`: This file.

## How to Use

1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/cancer-prediction-model.git
    cd cancer-prediction-model
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Prepare the data (adjust file paths and formatting if necessary):
    ```bash
    python src/data_preprocessing.py
    ```

4. Run the notebooks for exploratory data analysis and model training:
    - Launch Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
    - Execute the `notebooks/model_training.ipynb` to train the predictive model.

5. Evaluate the model using the test data:
    ```bash
    python src/evaluate_model.py
    ```

## Expected Outcomes

The predictive model is expected to accurately predict the presence of cancer based on the genomic data provided. Performance metrics such as **Accuracy**, **AUC-ROC**, and **F1-Score** will be employed to evaluate the model's efficacy.

## Contributions

Contributions are welcome. If you have suggestions or improvements for this project, please feel free to open an issue or submit a pull request.
