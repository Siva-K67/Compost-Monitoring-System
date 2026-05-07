import pandas as pd
import os

input_folder = "E:\IIIT Banglore\Compost Reading Data for Data Analytics COPY"
output_folder = "E:\IIIT Banglore\CSV FORMAT"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Convert each Excel file to CSV
for filename in os.listdir(input_folder):
    if filename.endswith(".xlsx"):  # Process only Excel files
        file_path = os.path.join(input_folder, filename)
        df = pd.read_excel(file_path)  # Read Excel
        csv_filename = filename.replace(".xlsx", ".csv")
        output_file_path = os.path.join(output_folder, csv_filename)
        df.to_csv(output_file_path, index=False)

print("Excel files converted to CSV!")
