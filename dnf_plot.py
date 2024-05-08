import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Fetch all the files from directory 
directory = './dnf_results/'
csv_files = [file for file in os.listdir(directory) if file.startswith('race_results_') and file.endswith('.csv')]

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each CSV file
for file in csv_files:
    filepath = os.path.join(directory, file)
    # Load each file into the dataframe
    df = pd.read_csv(filepath)
    # Set the race as the index
    df.set_index('Race', inplace=True)
    # Rename the DNF column to the year
    year = file.split('_')[-1].split('.')[0]
    df.rename(columns={'DNF': year}, inplace=True)
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, axis=1)

# Transpose the DataFrame so that races become columns and years become rows & sorting it by year
combined_df = combined_df.T
combined_df = combined_df[sorted(combined_df.columns)]

# Plotting
plt.figure(figsize=(12, 8))
sns.lineplot(data=combined_df.T, dashes=False)

plt.title('DNF Values by Year (2011-2021)')
plt.xlabel('Race')
plt.ylabel('Number of DNFs')
plt.xticks(rotation=90)
plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
