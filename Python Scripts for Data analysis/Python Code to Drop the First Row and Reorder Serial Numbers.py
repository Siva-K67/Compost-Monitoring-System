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
        
        # Check if the first row has any missing values and drop it
        if not df.empty and df.iloc[0].isnull().any():
            # Drop the first row
            df.drop(index=0, inplace=True)
        
        # Reorder the serial numbers ('S no' column)
        df['S no'] = range(1, len(df) + 1)  # Reassign serial numbers starting from 1
        
        # Save the modified data back to CSV (overwrite the original file or save as a new file)
        df.to_csv(file_path, index=False)
        
        print(f"First row dropped and serial numbers reordered for {filename}")

print("First rows dropped and serial numbers reordered for all CSV files.")
