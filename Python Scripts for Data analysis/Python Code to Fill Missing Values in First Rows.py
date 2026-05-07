import pandas as pd
import os

# Directory containing your CSV files
directory = 'E:\IIIT Banglore\FINAL'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Fill missing values in the first row with a specified method (e.g., forward fill or column mean)
        for col in df.columns:
            # Check if the first row has missing data
            if pd.isnull(df[col].iloc[0]):
                # Option 1: Forward fill (copy the next valid value)
                df[col].iloc[0] = df[col].iloc[1] if pd.notnull(df[col].iloc[1]) else 0
                
                # Option 2: Fill with the column mean (uncomment this if preferred)
                # df[col].iloc[0] = df[col].mean() if pd.notnull(df[col].iloc[0]) else df[col].mean()

        # Save the filled data back to CSV (overwrite the original file or save as a new file)
        df.to_csv(file_path, index=False)
        
        print(f"First row missing values filled for {filename}")

print("Missing values in first rows filled for all CSV files.")
