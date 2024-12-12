# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="box",
            order=study_time_order,
            )
# Show plot
plt.show()


# Create a box plot with subgroups and omit the outliers
#Add subgroups so each box plot is colored based on "location"
sns.catplot(x="internet", y="G3",
            data=student_data,
            kind="box",
            sym="",hue="location"
            )
# Show plot
plt.show()


# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)


# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])


