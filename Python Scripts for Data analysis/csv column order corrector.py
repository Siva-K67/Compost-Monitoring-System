import os
import pandas as pd

# Input and output folders
input_folder = "E:\IIIT Banglore\CSV FORMAT COPY"
output_folder = "E:\IIIT Banglore\CSV Ordered form"

# Desired column order
desired_columns = [
    "S no", "compost_temp", "pH_Value", "NH3", "H2S", "CH4", "soil_Moisture", "ambient_temp", "Humidity"
]

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each CSV file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        try:
            # Read the CSV file, skipping the first row if it's incorrect
            df = pd.read_csv(file_path, header=1)  # Skips the first row (row with "Unnamed")

            # Reorder columns and handle missing columns
            df = df.reindex(columns=desired_columns)
            
            # Save the cleaned CSV to the output folder
            output_path = os.path.join(output_folder, filename)
            df.to_csv(output_path, index=False)
            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

print("All files processed.")
