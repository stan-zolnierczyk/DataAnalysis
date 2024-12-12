"""
Using outer join to select actors
One cool aspect of using an outer join is that, because it returns all rows from both merged tables
and null where they do not match, you can use it to find rows that do not have a match in the other table.
To try for yourself, you have been given two tables with a list of actors from two popular movies:
Iron Man 1 and Iron Man 2. Most of the actors played in both movies. Use an outer join to find actors
who did not act in both movies.
"""

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     how='outer',
                                     on='id',
                                     suffixes=('_1','_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) |
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())