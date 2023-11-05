import pandas as pd

# Replace 'your_data.csv' with the path to your CSV file
csv_file = 'psychographic.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Display the first few rows of the DataFrame
print(df.head())

# Access data by column
tech_savvy_individuals = df[df['Tech_Savviness'] == 'Yes']
print("Tech-savvy individuals:")
print(tech_savvy_individuals)

# Calculate statistics
num_early_adopters = len(df[df['Early_Adopter'] == 'Yes'])
print(f"Number of early adopters: {num_early_adopters}")

# Filter data based on criteria
urban_dwellers = df[df['Urban_Dweller'] == 'Yes']
sustainability_advocates = df[df['Sustainability_Advocate'] == 'Yes']
print("Urban dwellers who are also sustainability advocates:")
print(urban_dwellers[urban_dwellers.index.isin(sustainability_advocates.index)])
