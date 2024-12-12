"""
Using .melt() to reshape government data
The US Bureau of Labor Statistics (BLS) often provides data series in an easy-to-read format
- it has a separate column for each month, and each year is a different row. Unfortunately,
this wide format makes it difficult to plot this information over time. In this exercise,
you will reshape a table of US unemployment rate data from the BLS into a form you can plot using .melt().
You will need to add a date column to the table and sort by it to plot the data correctly.

The unemployment rate data has been loaded for you in a table called ur_wide:
    year  jan  feb  mar  apr  ...  aug  sep  oct  nov  dec
0   2010  9.8  9.8  9.9  9.9  ...  9.5  9.5  9.4  9.8  9.3
1   2011  9.1  9.0  9.0  9.1  ...  9.0  9.0  8.8  8.6  8.5
2   2012  8.3  8.3  8.2  8.2  ...  8.1  7.8  7.8  7.7  7.9
3   2013  8.0  7.7  7.5  7.6  ...  7.2  7.2  7.2  6.9  6.7
4   2014  6.6  6.7  6.7  6.2  ...  6.1  5.9  5.7  5.8  5.6
5   2015  5.7  5.5  5.4  5.4  ...  5.1  5.0  5.0  5.1  5.0
6   2016  4.9  4.9  5.0  5.0  ...  4.9  5.0  4.9  4.7  4.7
7   2017  4.7  4.6  4.4  4.4  ...  4.4  4.2  4.1  4.2  4.1
8   2018  4.1  4.1  4.0  4.0  ...  3.8  3.7  3.8  3.7  3.9
9   2019  4.0  3.8  3.8  3.6  ...  3.7  3.5  3.6  3.5  3.5
10  2020  3.6  3.5  4.4  NaN  ...  NaN  NaN  NaN  NaN  NaN

[11 rows x 13 columns]
"""
# unpivot everything besides the year column
ur_tall = ur_wide.melt(id_vars='year', var_name='month', value_name='unempl_rate')


# Create a date column using the month and year columns of ur_tall
ur_tall['date'] = pd.to_datetime(ur_tall['year'] + '-' + ur_tall['month'])

# Sort ur_tall by date in ascending order
ur_sorted = ur_tall.sort_values(by='date',ascending=True)

# Plot the unempl_rate by date
ur_sorted.plot(x='date',y='unempl_rate')
plt.show()

"""
ur_sorted:
     year month  unempl_rate       date
0    2010   jan          9.8 2010-01-01
11   2010   feb          9.8 2010-02-01
22   2010   mar          9.9 2010-03-01
33   2010   apr          9.9 2010-04-01
44   2010   may          9.6 2010-05-01
..    ...   ...          ...        ...
87   2020   aug          NaN 2020-08-01
98   2020   sep          NaN 2020-09-01
109  2020   oct          NaN 2020-10-01
120  2020   nov          NaN 2020-11-01
131  2020   dec          NaN 2020-12-01

[132 rows x 4 columns]
"""