# Import both csv files, convert them to pandas dataframes

"""
You have been tasked with figuring out what the most popular types of fuel used in Chicago taxis are.
To complete the analysis, you need to merge the taxi_owners and taxi_veh tables together on the vid column.
You can then use the merged table along with the .value_counts() method to find the most common fuel_type
"""

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())