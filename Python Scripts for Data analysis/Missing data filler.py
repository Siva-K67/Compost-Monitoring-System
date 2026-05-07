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
        
        # Interpolate missing values linearly
        df.interpolate(method='linear', inplace=True)
        
        # Save the filled data back to CSV (overwrite the original file or save as new file)
        df.to_csv(file_path, index=False)
        
        print(f"Interpolation completed for {filename}")

print("Interpolation completed for all CSV files.")
