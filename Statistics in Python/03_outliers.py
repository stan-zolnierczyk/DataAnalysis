"""
Finding outliers using IQR
Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean,
such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread
that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than
Q1-1.5*IQR or greater than Q3+1.5*IQR, it's considered an outlier. In fact, this is how the lengths
of the whiskers in a matplotlib box plot are calculated.
"""

# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
"""
<script.py> output:
    country
    Albania      1777.85
    Algeria       707.88
    Angola        412.99
    Argentina    2172.40
    Armenia      1109.93
                  ...   
    Uruguay      1634.91
    Venezuela    1104.10
    Vietnam       641.51
    Zambia        225.30
    Zimbabwe      350.33
    Name: co2_emission, Length: 130, dtype: float64
"""