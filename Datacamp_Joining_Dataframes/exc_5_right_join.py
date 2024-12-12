"""
Right join to find unique movies
Most of the recent big-budget science fiction movies can also be classified as action movies.
You are given a table of science fiction movies called scifi_movies and another table of action movies
called action_movies. Your goal is to find which movies are considered only science fiction movies.
Once you have this table, you can merge the movies table in to see the movie names.
Since this exercise is related to science fiction movies, use a right join as your superhero power
to solve this problem.
"""

# Merge action_movies to the scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(scifi_only, left_on='id', right_on='movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

"""
      id                         title  popularity release_date  movie_id genre_act        genre_sci
0  18841  The Lost Skeleton of Cadavra       1.681   2001-09-12     18841       NaN  Science Fiction
1  26672     The Thief and the Cobbler       2.439   1993-09-23     26672       NaN  Science Fiction
2  15301      Twilight Zone: The Movie      12.903   1983-06-24     15301       NaN  Science Fiction
3   8452                   The 6th Day      18.447   2000-11-17      8452       NaN  Science Fiction
4   1649    Bill & Ted's Bogus Journey      11.350   1991-07-19      1649       NaN  Science Fiction
(258, 7)
"""