"""
Using merge_asof() to study stocks
You have a feed of stock market prices that you record. You attempt to track the price every five minutes.
Still, due to some network latency, the prices you record are roughly every 5 minutes.
You pull your price logs for three banks, JP Morgan (JPM), Wells Fargo (WFC), and Bank Of America (BAC).
You want to know how the price change of the two other banks compare to JP Morgan.
Therefore, you will need to merge these three logs into one table. Afterward, you will use
the pandas .diff() method to compute the price change over time. Finally, plot the price changes
so you can review your analysis.
"""

# Use merge_asof() to merge jpm and wells
jpm_wells = pd.merge_asof(jpm,wells,on='date_time', direction='nearest', suffixes=('', '_wells'))


# Use merge_asof() to merge jpm_wells and bac
jpm_wells_bac = pd.merge_asof(jpm_wells,bac,on='date_time', direction='nearest', suffixes=('_jpm', '_bac'))


# Compute price diff
price_diffs = jpm_wells_bac.diff()

# Plot the price diff of the close of jpm, wells and bac only
price_diffs.plot(y=['close_jpm', 'close_wells', 'close_bac'])
plt.show()

"""
         date_time  close_jpm  close_wells  close_bac
0              NaT        NaN          NaN        NaN
1  0 days 00:04:47      0.060       -0.003      0.000
2  0 days 00:04:57     -0.449       -0.130     -0.164
3  0 days 00:05:54      0.009       -0.020     -0.010
4  0 days 00:04:05      0.075        0.014      0.005
5  0 days 00:05:30      0.205        0.081      0.069
6  0 days 00:04:37     -0.220       -0.065     -0.079
7  0 days 00:05:01      0.040       -0.045      0.015
8  0 days 00:05:03     -0.130        0.035     -0.019
9  0 days 00:05:18      0.050        0.015      0.019
10 0 days 00:04:56      0.060        0.025      0.079
11 0 days 00:05:28      0.130       -0.010      0.015
12 0 days 00:04:18      0.040        0.000      0.010
13 0 days 00:05:33      0.070        0.060      0.035
14 0 days 00:05:08     -0.010       -0.040     -0.005
15 0 days 00:04:45      0.060       -0.070      0.025
16 0 days 00:04:25      0.070        0.010      0.020
"""