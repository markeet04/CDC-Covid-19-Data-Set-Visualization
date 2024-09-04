import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the JSON data into a DataFrame
with open('total_deaths_by_state.json') as f:
    data = json.load(f)

# Convert the JSON data into a pandas DataFrame
df = pd.DataFrame(data)

# Set the 'state' column as the index
df.set_index('state', inplace=True)

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df[['total_deaths']], annot=True, fmt=".1f", cmap="YlGnBu", linewidths=.5)

# Save the heatmap to a file
plt.savefig('static/heatmap.png')

# Show the heatmap
plt.show()
