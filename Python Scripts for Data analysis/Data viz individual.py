import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Directory containing your CSV files
directory = 'E:\IIIT Banglore\Alternative FINAL'
#dir='E:\IIIT Banglore\FINAL_HALF\analysis_results'

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
        
        # Show basic statistics for the current file
        print(f"Basic Statistics for {filename}:")
        print(df.describe())
        print("\n")
        
        # Check for missing values
        print(f"Missing Values for {filename}:")
        print(df.isnull().sum())
        print("\n")
        
        # Correlation between columns (numerical)
        print(f"Correlation Matrix for {filename}:")
        print(df.corr())
        print("\n")

        # Save analysis results to a new CSV (optional)
        #df.to_csv(f"{dir}/cleaned_{filename}", index=False)
        
        # Visualization 1: Pairplot of some columns (e.g., compost_temp, pH_Value, NH3, H2S, CH4)
        sns.pairplot(df[['compost_temp', 'pH_Value', 'NH3', 'H2S', 'CH4']])
        plt.title(f"Pairplot for {filename}")
        plt.savefig(f"{directory}/{filename}_pairplot.png")  # Save the plot as a PNG image
        plt.clf()  # Clear the current plot to avoid overlap with the next
        plt.close()

        # Visualization 2: Histogram of 'compost_temp'
        plt.figure(figsize=(10, 6))
        plt.hist(df['compost_temp'], bins=30, color='blue', alpha=0.7)
        plt.title(f"Distribution of Compost Temperature for {filename}")
        plt.xlabel('Compost Temperature')
        plt.ylabel('Frequency')
        plt.savefig(f"{directory}/{filename}_compost_temp_histogram.png")  # Save as image
        plt.clf()  # Clear plot
        plt.close()
        
        # Visualization 3: Correlation heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title(f"Correlation Heatmap for {filename}")
        plt.savefig(f"{directory}/{filename}_correlation_heatmap.png")  # Save as image
        plt.clf()  # Clear plot
        plt.close()

        # Visualization 4: Box Plot (Whisker Plot) for All Columns
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=df.drop(columns=["S no"]))  # Drop 'S no' as it is not relevant for box plot
        plt.title(f"Boxplot (Whisker Plot) for {filename}", fontsize=16)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{directory}/{filename}_boxplot_all_columns.png")  # Save as image
        plt.clf()  # Clear plot
        plt.close()

        # Visualization 5: Individual Box Plots for Each Column
        for column in df.columns[1:]:  # Skip 'S no'
            plt.figure(figsize=(10, 6))
            sns.boxplot(y=df[column], color='skyblue')
            plt.title(f"Boxplot for {column} in {filename}", fontsize=16)
            plt.ylabel(column)
            plt.tight_layout()
            plt.savefig(f"{directory}/{filename}_{column}_boxplot.png")  # Save as image
            plt.clf()  # Clear plot
            plt.close()
        
        print(f"Analysis completed for {filename}")
        print("-" * 50)

print("Data analysis completed for all CSV files.")
