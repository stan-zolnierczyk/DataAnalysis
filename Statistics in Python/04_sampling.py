"""
Sampling deals
In the previous exercise, you counted the deals Amir worked on. Now it's time to randomly pick
five deals so that you can reach out to each customer and ask if they were satisfied with the service
they received. You'll try doing this both with and without replacement.

Additionally, you want to make sure this is done randomly and that it can be reproduced
in case you get asked how you chose the deals, so you'll need to set the random seed before sampling
from the deals.
"""

# Set random seed
np.random.seed(13)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5, replace=False)
print(sample_without_replacement)
"""
     Unnamed: 0    product   client status   amount  num_users
145         146  Product A  Current    Won  4682.94         63
7             8  Product N  Current    Won  7340.64         13
150         151  Product D  Current   Lost  7550.60         17
110         111  Product B  Current    Won   696.88         44
104         105  Product D  Current    Won  4110.98         39
"""