# Set the style to "whitegrid"
sns.set_style("whitegrid")
# Preset options: "white", "dark", "whitegrid", "darkgrid", "ticks"

# Set the color palette to "Purples"
sns.set_palette("Purples")


# Changing the scale
sns.set_context("paper")
# Smallest to largest: "paper", "notebook", "talk", "poster"

"""
FacetGrids vs. AxesSubplots
In the recent lesson, we learned that Seaborn plot functions create two different types of objects: 
FacetGrid objects and AxesSubplot objects. The method for adding a title to your plot will differ 
depending on the type of object it is.
"""

# Przykład dla relplot i catplot (FacetGrid)
# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")
# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")
# Add labels
g.set(xlabel="Location of Residence",
       ylabel="% Who Like Techno")


# Przykład dla pozostałych (AxesSubplots)
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean",
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel="Car Model Year",
ylabel="Average MPG")

# Rotate x-tick labels
plt.xticks(rotation=90)