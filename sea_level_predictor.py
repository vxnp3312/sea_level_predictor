import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#import the data from epa-sea-level.csv
df = pd.read_csv('epa-sea-level.csv')
df.head()

#Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis
plt.figure(figsize=(14, 4))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.title('CSIRO Adjusted Sea Level')
plt.show()

#get the slope and y-intercept of the line of best fit. 
#Plot the line of best fit over the top of the scatter plot
plt.figure(figsize=(14, 4))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
line_fit = [slope * year + intercept for year in range(1880, 2051)]
plt.plot(range(1880, 2051), line_fit, label='Line of Best Fit (1880-2050)')

#Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

#Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
line_fit_recent = [slope_recent * year + intercept_recent for year in range(2000, 2051)]
plt.plot(range(2000, 2051), line_fit_recent, label='Line of Best Fit (2000-2050)')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()

# Save and return the plot
plt.savefig('sea_level_plot.png')
plt.show()
