"""
Performing an anti join
In our music streaming company dataset, each customer is assigned an employee representative to assist them.
In this exercise, filter the employee table by a table of top customers, returning only those employees
who are not assigned to a customer. The results should resemble the results of an anti join.
The company's leadership will assign these employees additional training so that they can work
with high valued customers.
"""
# Merge employees and top_cust
empl_cust = employees.merge(top_cust, on='srid',
                                 how='left', indicator=True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])