import pandas as pd

# Read the csv file in
cities_df = pd.read_csv('Resources/cities.csv')

# Save to file
cities_df.to_html('data_table.html', index=False)

