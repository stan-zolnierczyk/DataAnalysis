"""
Quartiles, quantiles, and quintiles
Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread,
as well as to get a sense of where a data point stands in relation to the rest of the data set.
For example, you might want to give a discount to the 10% most active users on a website.

In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset
into 4, 5, and 10 pieces, respectively.
"""

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0,0.25,0.5,0.75,1]))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0,0.2,0.4,0.6,0.8,1]))
"""
[   0.       3.54    11.026   25.59    99.978 1712.   ]
"""

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)
"""
<script.py> output:
    country
    Argentina    2172.4
    Name: co2_emission, dtype: float64
"""