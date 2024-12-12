"""
One-to-many merge with multiple tables
In this exercise, assume that you are looking to start a business in the city of Chicago.
Your perfect idea is to start a company that uses goats to mow the lawn for other businesses.
However, you have to choose a location in the city to put your goat farm.
You need a location with a great deal of space and relatively few businesses and people around
to avoid complaints about the smell. You will need to merge three tables to help you choose your location.
The land_use table has info on the percentage of vacant land by city ward. The census table has population by ward,
and the licenses table lists businesses by ward.
"""

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(census, on='ward') \
                    .merge(licenses, on='ward', suffixes=('_cen','_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward','pop_2010','vacant'],
                                   as_index=False).agg({'account':'count'})

# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(by=['vacant','account','pop_2010'],
                                             ascending=[False,True,True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())