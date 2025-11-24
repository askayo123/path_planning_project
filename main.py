import pandas as pd
import os

file_path= 'data\BrandsHatchLayout.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Data loaded successfully.")  
    print(df.to_string())

else:
    print(f"File not found: {file_path}")