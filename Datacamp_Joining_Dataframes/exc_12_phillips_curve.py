"""
Phillips curve using merge_ordered()
There is an economic theory developed by A. W. Phillips which states that inflation and unemployment
have an inverse relationship. The theory claims that with economic growth comes inflation,
which in turn should lead to more jobs and less unemployment.
You will take two tables of data from the U.S. Bureau of Labor Statistics, containing unemployment
and inflation data over different periods, and create a Phillips curve. The tables have different frequencies.
One table has a data entry every six months, while the other has a data entry every month.
You will need to use the entries where you have data within both tables.
"""

# Use merge_ordered() to merge inflation, unemployment with inner join
inflation_unemploy = pd.merge_ordered(inflation, unemployment, left_on='date', right_on='date',how='inner',  fill_method='ffill')

# Print inflation_unemploy
print(inflation_unemploy)

# Plot a scatter plot of unemployment_rate vs cpi of inflation_unemploy
inflation_unemploy.plot(kind='scatter',x='unemployment_rate' ,y='cpi')
plt.show()

"""
<script.py> output:
             date      cpi     seriesid                  data_type  unemployment_rate
    0  2014-01-01  235.288  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                6.7
    1  2014-06-01  237.231  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                6.1
    2  2015-01-01  234.718  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.6
    3  2015-06-01  237.684  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.3
    4  2016-01-01  237.833  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                5.0
    5  2016-06-01  240.167  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.9
    6  2017-01-01  243.780  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.7
    7  2017-06-01  244.182  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.3
    8  2018-01-01  248.884  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.1
    9  2018-06-01  251.134  CUSR0000SA0  SEASONALLY ADJUSTED INDEX                4.0
"""