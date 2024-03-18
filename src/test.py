import matplotlib.pyplot as plt

# Generate some sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Plot the data
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
asdad=765754

# Add text under the plot
plt.text(3, max(y)+1, f'This is some text under the plot{asdad}', ha='center')

plt.show()