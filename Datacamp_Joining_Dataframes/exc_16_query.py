"""
Subsetting rows with .query()
In this exercise, you will revisit GDP and population data for Australia and Sweden from the World Bank
and expand on it using the .query() method. You'll merge the two tables and compute the GDP per capita.
Afterwards, you'll use the .query() method to sub-select the rows and create a plot.
Recall that you will need to merge on multiple columns in the proper order.
"""

"""
gdp:
        date    country         gdp    series_code
0  1990-01-01  Australia  158051.132  NYGDPMKTPSAKD
1  1990-04-01  Australia  158263.582  NYGDPMKTPSAKD
2  1990-07-01  Australia  157329.279  NYGDPMKTPSAKD
3  1990-09-01  Australia  158240.678  NYGDPMKTPSAKD
4  1991-01-01  Australia  156195.954  NYGDPMKTPSAKD
5  1991-04-01  Australia  155989.033  NYGDPMKTPSAKD
6  1991-07-01  Australia  156635.858  NYGDPMKTPSAKD
7  1991-09-01  Australia  156744.057  NYGDPMKTPSAKD
8  1992-01-01  Australia  157916.081  NYGDPMKTPSAKD
9  1992-04-01  Australia  159047.827  NYGDPMKTPSAKD
10 1992-07-01  Australia  160658.176  NYGDPMKTPSAKD
11 1992-09-01  Australia  163960.221  NYGDPMKTPSAKD
12 1993-01-01  Australia  165097.495  NYGDPMKTPSAKD
13 1993-04-01  Australia  166027.059  NYGDPMKTPSAKD
14 1993-07-01  Australia  166203.179  NYGDPMKTPSAKD
15 1993-09-01  Australia  169279.348  NYGDPMKTPSAKD
16 1990-01-01     Sweden   79837.846  NYGDPMKTPSAKD
17 1990-04-01     Sweden   80582.286  NYGDPMKTPSAKD
18 1990-07-01     Sweden   79974.360  NYGDPMKTPSAKD
19 1990-09-01     Sweden   80106.497  NYGDPMKTPSAKD
20 1991-01-01     Sweden   79524.242  NYGDPMKTPSAKD
21 1991-04-01     Sweden   79073.059  NYGDPMKTPSAKD
22 1991-07-01     Sweden   79084.770  NYGDPMKTPSAKD
23 1991-09-01     Sweden   79740.606  NYGDPMKTPSAKD
24 1992-01-01     Sweden   79390.922  NYGDPMKTPSAKD
25 1992-04-01     Sweden   79060.283  NYGDPMKTPSAKD
26 1992-07-01     Sweden   78904.605  NYGDPMKTPSAKD
27 1992-09-01     Sweden   76996.837  NYGDPMKTPSAKD
28 1993-01-01     Sweden   75783.588  NYGDPMKTPSAKD
29 1993-04-01     Sweden   76708.548  NYGDPMKTPSAKD
30 1993-07-01     Sweden   77662.018  NYGDPMKTPSAKD
31 1993-09-01     Sweden   77703.304  NYGDPMKTPSAKD

pop:
date    country       pop  series_code
0 1990-01-01  Australia  17065100  SP.POP.TOTL
1 1991-01-01  Australia  17284000  SP.POP.TOTL
2 1992-01-01  Australia  17495000  SP.POP.TOTL
3 1993-01-01  Australia  17667000  SP.POP.TOTL
4 1990-01-01     Sweden   8558835  SP.POP.TOTL
5 1991-01-01     Sweden   8617375  SP.POP.TOTL
6 1992-01-01     Sweden   8668067  SP.POP.TOTL
7 1993-01-01     Sweden   8718561  SP.POP.TOTL
"""

# Merge gdp and pop on date and country with fill
gdp_pop = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')

# Add a column named gdp_per_capita to gdp_pop that divides the gdp by pop
gdp_pop['gdp_per_capita'] = gdp_pop['gdp'] / gdp_pop['pop']

# Pivot data so gdp_per_capita, where index is date and columns is country
gdp_pivot = gdp_pop.pivot_table('gdp_per_capita', 'date', 'country')

# Select dates equal to or greater than 1991-01-01
recent_gdp_pop = gdp_pivot.query('date >= "1991-01-01"')

# Plot recent_gdp_pop
recent_gdp_pop.plot(rot=90)
plt.show()

"""
recent_gdp_pop:
country     Australia  Sweden
date                         
1991-01-01      0.009   0.009
1991-04-01      0.009   0.009
1991-07-01      0.009   0.009
1991-09-01      0.009   0.009
1992-01-01      0.009   0.009
1992-04-01      0.009   0.009
1992-07-01      0.009   0.009
1992-09-01      0.009   0.009
1993-01-01      0.009   0.009
1993-04-01      0.009   0.009
1993-07-01      0.009   0.009
1993-09-01      0.010   0.009
"""