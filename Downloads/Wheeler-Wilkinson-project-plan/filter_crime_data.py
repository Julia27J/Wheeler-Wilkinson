import pandas as pd

# Load the CSV
df = pd.read_csv('Chicago_Crime_Dataset_2020.csv')

# Filter for Year 2020 (in case there are others)
df = df[df['Year'] == 2020]

# Select important columns
important_columns = [
    'Date', 'Primary Type', 'Description', 'Location Description',
    'Arrest', 'Domestic', 'Beat', 'District', 'Ward', 'Community Area',
    'Latitude', 'Longitude'
]
df_filtered = df[important_columns]

# Save to new CSV
df_filtered.to_csv('Chicago_Crime_2020_filtered.csv', index=False)

print(f"Filtered dataset saved with {len(df_filtered)} rows and {len(important_columns)} columns.")