# Create a point plot of family relationship vs. absences
# Add caps to the confidence interval
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2,
            join=False)
# Show plot
plt.show()



# Create a point plot that uses color to create subgroups
# Turn off the confidence intervals for this plot
# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)
# Show plot
plt.show()