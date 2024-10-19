import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
import numpy as np

def smote_data_generation(file_path, num_samples=10):
    try:
        excel_data = pd.ExcelFile(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    for sheet_name in excel_data.sheet_names:
        print(f"Processing sheet: {sheet_name}")
        df = pd.read_excel(excel_data, sheet_name=sheet_name)

        target_column = df.columns[-1]
        if df[target_column].dtype not in ['int64', 'float64', 'object']:
            print(f"Skipping sheet {sheet_name} as the target column is not suitable for SMOTE.")
            continue

        if df[target_column].dtype == 'object':
            le = LabelEncoder()
            df[target_column] = le.fit_transform(df[target_column])

        X = df.drop(columns=[target_column])
        y = df[target_column]

        X = pd.get_dummies(X, drop_first=True)

        smote = SMOTE(sampling_strategy='auto', random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X, y)

        resampled_df = pd.DataFrame(X_resampled, columns=X.columns)
        resampled_df[target_column] = y_resampled

        if 'le' in locals():
            resampled_df[target_column] = le.inverse_transform(resampled_df[target_column].astype(int))

        output_file = 'ResampledData.xlsx'
        with pd.ExcelWriter(output_file, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
            resampled_df.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"SMOTE applied and data saved for sheet: {sheet_name}")

    print(f"Data generation with SMOTE completed. Check '{output_file}'.")

file_path = "/mnt/data/ElectronicsStore-DatabaseExport.xls"
num_samples = 20
smote_data_generation(file_path, num_samples)
