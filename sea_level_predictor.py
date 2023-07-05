import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    years_future = range(int(df['Year'].iloc[0]), 2051)
    result_1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    m1 = result_1.slope
    c1 = result_1.intercept
    plt.plot(years_future, m1*years_future + c1)
  
    # Create second line of best fit

    df_2000 = df[df['Year'] >= 2000]
    result_2 = linregress(x=df_2000['Year'], y=df_2000['CSIRO Adjusted Sea Level'])
    m2 = result_2.slope
    c2 = result_2.intercept
    years_from2000 = range(int(df_2000['Year'].iloc[0]), 2051)
    plt.plot(years_from2000, m2*years_from2000 + c2)
  
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()