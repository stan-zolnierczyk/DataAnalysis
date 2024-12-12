"""
Creating a probability distribution
A new restaurant opened a few months ago, and the restaurant's management wants to optimize its seating space
 based on the size of the groups that come most often. On one night, there are 10 groups of people waiting
 to be seated at the restaurant, but instead of being called in the order they arrived, they will be called
 randomly. In this exercise, you'll investigate the probability of groups of different sizes
 getting picked first. Data on each of the ten groups is contained in the restaurant_groups DataFrame

 group_id  group_size
0        A           2
1        B           4
2        C           6
3        D           2
4        E           2
5        F           2
6        G           3
7        H           2
8        I           4
9        J           2
"""
# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

# Calculate expected value
expected_value = np.sum(size_dist['group_size']*size_dist['prob'])
print(expected_value)
# 2.9000000000000004

# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)
# 0.30000000000000004