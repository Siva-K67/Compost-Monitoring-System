import os
import pandas as pd

# Input and output folder paths
input_folder = "E:\IIIT Banglore\CSV Ordered form"  # Replace with the folder containing your CSV files
output_folder = "E:\IIIT Banglore\FINAL"  # Replace with the folder where you want to save cleaned files

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process all CSV files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".csv"):  # Process only CSV files
        file_path = os.path.join(input_folder, file_name)
        
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Remove empty rows
        df_cleaned = df.dropna(how="all")  # This removes rows where all elements are NaN
        
        # Save the cleaned file to the output folder
        cleaned_file_path = os.path.join(output_folder, file_name)
        df_cleaned.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned file saved: {cleaned_file_path}")

print("All files have been processed.")