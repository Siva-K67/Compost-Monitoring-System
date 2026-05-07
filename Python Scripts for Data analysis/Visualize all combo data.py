import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Directory containing your CSV files
directory = 'E:\IIIT Banglore\FINAL'

# List to store all DataFrames
dfs = []

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        
        # Load the CSV file
        df = pd.read_csv(file_path)
        
        # Clean the data if necessary (e.g., drop first row with missing values)
        if df.iloc[0].isnull().any():
            df.drop(index=0, inplace=True)
        
        # Reassign serial numbers to start from 1
        df['S no'] = range(1, len(df) + 1)
        
        # Add the DataFrame to the list
        dfs.append(df)

# Concatenate all DataFrames into one large DataFrame
all_data = pd.concat(dfs, ignore_index=True)

# Show basic statistics
print("Basic Statistics:")
print(all_data.describe())

# Check for missing values
print("\nMissing Values:")
print(all_data.isnull().sum())

# Correlation between columns (numerical)
print("\nCorrelation Matrix:")
print(all_data.corr())

# Visualization Example 1: Pairplot of some columns
sns.pairplot(all_data[['compost_temp', 'pH_Value', 'NH3', 'H2S', 'CH4']])
plt.show()

# Visualization Example 2: Histogram of 'compost_temp'
plt.figure(figsize=(10, 6))
plt.hist(all_data['compost_temp'], bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Compost Temperature')
plt.xlabel('Compost Temperature')
plt.ylabel('Frequency')
plt.show()

# Visualization Example 3: Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(all_data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

