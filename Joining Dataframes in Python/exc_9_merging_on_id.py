"""
Do sequels earn more?
It is time to put together many of the aspects that you have learned in this chapter. In this exercise,
you'll find out which movie sequels earned the most compared to the original movie. To answer this question,
you will merge a modified version of the sequels and financials tables where their index is the movie ID.
You will need to choose a merge type that will return all of the rows from the sequels table
and not all the rows of financials table need to be included in the result. From there,
you will join the resulting table to itself so that you can compare the revenue values of the original movie
to the sequel. Next, you will calculate the difference between the two revenues and sort the resulting dataset.
"""

# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel',
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff
titles_diff = orig_seq[['title_org','title_seq','diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values(by='diff',ascending=False).head())

