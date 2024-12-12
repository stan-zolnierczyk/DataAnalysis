"""
Self join
Merging a table to itself can be useful when you want to compare values in a column to other values
in the same column. In this exercise, you will practice this by creating a table that for each movie
will list the movie director and a member of the crew on one row. You have been given a table called crews,
which has columns id, job, and name. First, merge the table to itself using the movie ID.
This merge will give you a larger table where for each movie, every job is matched against each other.
Then select only those rows with a director in the left table, and avoid having a row
where the director's job is listed in both the left and right tables.
This filtering will remove job combinations that aren't with the director.
"""

# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

"""
        id   job_dir       name_dir        job_crew          name_crew
156  19995  Director  James Cameron          Editor  Stephen E. Rivkin
157  19995  Director  James Cameron  Sound Designer  Christopher Boyes
158  19995  Director  James Cameron         Casting          Mali Finn
160  19995  Director  James Cameron          Writer      James Cameron
161  19995  Director  James Cameron    Set Designer    Richard F. Mays
"""