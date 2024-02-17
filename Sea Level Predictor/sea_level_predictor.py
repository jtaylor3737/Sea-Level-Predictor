import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# getlines isnt getting lines lol, result is good but need to understand unit test
def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    first_line_years = list(df["Year"])
    new_years = list(range(2014, 2051))
    for x in new_years:
        first_line_years.append(x)
    slope, intercept, r, p, std_error = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )
    first_line = []
    for x in first_line_years:
        first_line.append(slope * x + intercept)
    plt.plot(first_line_years, first_line)

    # Create second line of best fit
    df_2 = df[df["Year"] > 1999]
    slope, intercept, r, p, std_error = linregress(
        df_2["Year"], df_2["CSIRO Adjusted Sea Level"]
    )
    second_line = []
    second_line_years = list(range(2000, 2051))
    for x in second_line_years:
        second_line.append(slope * x + intercept)
    plt.plot(second_line_years, second_line)

    # Add labels and title
    plt.ylabel("Sea Level (inches)")
    plt.xlabel("Year")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
