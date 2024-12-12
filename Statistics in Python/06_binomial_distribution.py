"""
Simulating sales deals
Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on.
Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals
with a binomial distribution. In this exercise, you'll help Amir simulate a year's worth of his deals
so he can better understand his performance.
"""
# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)

# Print mean deals won per week
print(np.mean(deals))

# 0.8269230769230769