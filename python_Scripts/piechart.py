import matplotlib.pyplot as plt
import pandas as pd
import json

# Load the data from the JSON file
with open('total_deaths_by_age_group.json') as f:
    data = json.load(f)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Filter out the 'All Ages' group if it's present
df = df[df['age_group'] != 'All Ages']

# Sort the data by total_deaths for better visualization
df = df.sort_values(by='total_deaths', ascending=False)

# Create the pie chart
plt.figure(figsize=(14, 10))
plt.pie(
    df['total_deaths'],
    labels=df['age_group'],
    autopct='%1.1f%%',
    colors=plt.cm.Paired.colors,
    startangle=400,
    wedgeprops=dict(width=0.8, edgecolor='w'),  # Make the pie wider
    textprops={'fontsize': 10},  # Adjust the font size of labels
    labeldistance=1.5,  # Increase the distance of the labels from the center
    pctdistance=.85    # Increase the distance of the percentages from the center
)

# Add a legend and a title
plt.title('Total Deaths by Age Group', fontsize=16)
plt.legend(
    df['age_group'],
    title='Age Groups',
    loc='center left',
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Show the pie chart
plt.tight_layout()
plt.show()
