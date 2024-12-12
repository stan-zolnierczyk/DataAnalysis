# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender', y="Interested in Math", data=survey_data,
            kind="bar")
# Show plot
plt.show()



# List of categories from lowest to highest
category_order = ["<2 hours",
                  "2 to 5 hours",
                  "5 to 10 hours",
                  ">10 hours"]
# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order)
# Show plot
plt.show()


# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            ci=None)
# Show plot
plt.show()