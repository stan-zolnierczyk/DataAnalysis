"""
Using .melt() for stocks vs bond performance
It is widespread knowledge that the price of bonds is inversely related to the price of stocks.
In this last exercise, you'll review many of the topics in this chapter to confirm this.
You have been given a table of percent change of the US 10-year treasury bond price.
It is in a wide format where there is a separate column for each year.
You will need to use the .melt() method to reshape this table.

Additionally, you will use the .query() method to filter out unneeded data. You will merge this table
with a table of the percent change of the Dow Jones Industrial stock index price.
Finally, you will plot data.

ten_yr :
metric  2007-02-01  2007-03-01  2007-04-01  2007-05-01  ...  2009-08-01  2009-09-01  2009-10-01  2009-11-01  2009-12-01
0   open       0.033      -0.060       0.025      -0.004  ...      -0.007      -0.047      -0.032       0.034      -0.051
1   high      -0.007      -0.041       0.022       0.031  ...       0.032      -0.090       0.012      -0.004       0.099
2    low      -0.016      -0.008       0.031      -0.002  ...       0.040      -0.036      -0.051       0.030       0.007
3  close      -0.057       0.022      -0.004       0.056  ...      -0.029      -0.028       0.026      -0.056       0.201
[4 rows x 36 columns]

dji:
           date  close
0    2007-02-01  0.005
1    2007-03-01 -0.026
2    2007-04-01  0.049
3    2007-05-01  0.052
4    2007-06-01 -0.016
..          ...    ...
154  2019-12-01    NaN
155  2020-01-01    NaN
156  2020-02-01 -0.010
157  2020-03-01 -0.216
158  2020-04-01  0.035
[159 rows x 2 columns]
"""
# Use melt on ten_yr, unpivot everything besides the metric column
bond_perc = ten_yr.melt(id_vars='metric', var_name='date', value_name='close')

# Use query on bond_perc to select only the rows where metric=close
bond_perc_close = bond_perc.query('metric=="close"')

# Merge (ordered) dji and bond_perc_close on date with an inner join
dow_bond = pd.merge_ordered(dji,bond_perc_close,on='date',how='inner',suffixes =('_dow', '_bond'))


# Plot only the close_dow and close_bond columns
dow_bond.plot(y=['close_dow','close_bond'], x='date', rot=90)
plt.show()

"""
dow_bond:
          date  close_dow metric  close_bond
0   2007-02-01      0.005  close      -0.057
1   2007-03-01     -0.026  close       0.022
2   2007-04-01      0.049  close      -0.004
3   2007-05-01      0.052  close       0.056
4   2007-06-01     -0.016  close       0.029
5   2007-07-01      0.038  close      -0.052
6   2007-08-01     -0.064  close      -0.049
7   2007-09-01      0.067  close       0.009
8   2007-10-01      0.002  close      -0.023
9   2007-11-01     -0.024  close      -0.112
10  2007-12-01     -0.011  close       0.016
11  2008-01-01     -0.059  close      -0.098
12  2008-02-01     -0.036  close      -0.029
13  2008-03-01      0.013  close      -0.029
14  2008-04-01      0.021  close       0.095
15  2008-05-01     -0.001  close       0.076
16  2008-06-01     -0.043  close      -0.017
17  2008-07-01     -0.057  close       0.000
18  2008-08-01      0.025  close      -0.042
19  2008-09-01     -0.069  close       0.004
20  2008-10-01     -0.154  close       0.037
21  2008-11-01     -0.080  close      -0.255
22  2008-12-01      0.058  close      -0.241
23  2009-01-01     -0.037  close       0.267
24  2009-02-01     -0.165  close       0.069
25  2009-03-01      0.042  close      -0.117
26  2009-04-01      0.065  close       0.164
27  2009-05-01      0.057  close       0.109
28  2009-06-01      0.039  close       0.017
29  2009-07-01     -0.048  close      -0.006
30  2009-08-01      0.111  close      -0.029
31  2009-09-01      0.058  close      -0.028
32  2009-10-01     -0.008  close       0.026
33  2009-11-01      0.077  close      -0.056
34  2009-12-01     -0.003  close       0.201
"""
