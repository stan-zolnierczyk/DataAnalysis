"""
merge_ordered() caution, multiple columns
When using merge_ordered() to merge on multiple columns, the order is important when you combine it
with the forward fill feature. The function sorts the merge on columns in the order provided.
In this exercise, we will merge GDP and population data from the World Bank for Australia and Sweden,
reversing the order of the merge on columns. The frequency of the series are different, the GDP values
are quarterly, and the population is yearly. Use the forward fill feature to fill in the missing data.
Depending on the order provided, the fill forward will use unintended data to fill in the missing values.
"""

# Merge gdp and pop on date and country with fill and notice rows 2 and 3
ctry_date = pd.merge_ordered(gdp, pop, on=['date','country'], fill_method='ffill')
# Print ctry_date
print(ctry_date)
"""
         date    country         gdp  series_code_x       pop series_code_y
0  1990-01-01  Australia  158051.132  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
1  1990-01-01     Sweden   79837.846  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
2  1990-04-01  Australia  158263.582  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
3  1990-04-01     Sweden   80582.286  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
4  1990-07-01  Australia  157329.279  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
5  1990-07-01     Sweden   79974.360  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
6  1990-09-01  Australia  158240.678  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
7  1990-09-01     Sweden   80106.497  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
8  1991-01-01  Australia  156195.954  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
9  1991-01-01     Sweden   79524.242  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
10 1991-04-01  Australia  155989.033  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
11 1991-04-01     Sweden   79073.059  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
12 1991-07-01  Australia  156635.858  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
13 1991-07-01     Sweden   79084.770  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
14 1991-09-01  Australia  156744.057  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
15 1991-09-01     Sweden   79740.606  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
16 1992-01-01  Australia  157916.081  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
17 1992-01-01     Sweden   79390.922  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
18 1992-04-01  Australia  159047.827  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
19 1992-04-01     Sweden   79060.283  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
20 1992-07-01  Australia  160658.176  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
21 1992-07-01     Sweden   78904.605  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
22 1992-09-01  Australia  163960.221  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
23 1992-09-01     Sweden   76996.837  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
24 1993-01-01  Australia  165097.495  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
25 1993-01-01     Sweden   75783.588  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
26 1993-04-01  Australia  166027.059  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
27 1993-04-01     Sweden   76708.548  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
28 1993-07-01  Australia  166203.179  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
29 1993-07-01     Sweden   77662.018  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
30 1993-09-01  Australia  169279.348  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
31 1993-09-01     Sweden   77703.304  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
"""

# Merge gdp and pop on country and date with fill
date_ctry = pd.merge_ordered(gdp, pop, on=['country','date'], fill_method='ffill')
# Print date_ctry
print(date_ctry)
"""
         date    country         gdp  series_code_x       pop series_code_y
0  1990-01-01  Australia  158051.132  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
1  1990-04-01  Australia  158263.582  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
2  1990-07-01  Australia  157329.279  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
3  1990-09-01  Australia  158240.678  NYGDPMKTPSAKD  17065100   SP.POP.TOTL
4  1991-01-01  Australia  156195.954  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
5  1991-04-01  Australia  155989.033  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
6  1991-07-01  Australia  156635.858  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
7  1991-09-01  Australia  156744.057  NYGDPMKTPSAKD  17284000   SP.POP.TOTL
8  1992-01-01  Australia  157916.081  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
9  1992-04-01  Australia  159047.827  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
10 1992-07-01  Australia  160658.176  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
11 1992-09-01  Australia  163960.221  NYGDPMKTPSAKD  17495000   SP.POP.TOTL
12 1993-01-01  Australia  165097.495  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
13 1993-04-01  Australia  166027.059  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
14 1993-07-01  Australia  166203.179  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
15 1993-09-01  Australia  169279.348  NYGDPMKTPSAKD  17667000   SP.POP.TOTL
16 1990-01-01     Sweden   79837.846  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
17 1990-04-01     Sweden   80582.286  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
18 1990-07-01     Sweden   79974.360  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
19 1990-09-01     Sweden   80106.497  NYGDPMKTPSAKD   8558835   SP.POP.TOTL
20 1991-01-01     Sweden   79524.242  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
21 1991-04-01     Sweden   79073.059  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
22 1991-07-01     Sweden   79084.770  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
23 1991-09-01     Sweden   79740.606  NYGDPMKTPSAKD   8617375   SP.POP.TOTL
24 1992-01-01     Sweden   79390.922  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
25 1992-04-01     Sweden   79060.283  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
26 1992-07-01     Sweden   78904.605  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
27 1992-09-01     Sweden   76996.837  NYGDPMKTPSAKD   8668067   SP.POP.TOTL
28 1993-01-01     Sweden   75783.588  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
29 1993-04-01     Sweden   76708.548  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
30 1993-07-01     Sweden   77662.018  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
31 1993-09-01     Sweden   77703.304  NYGDPMKTPSAKD   8718561   SP.POP.TOTL
"""
