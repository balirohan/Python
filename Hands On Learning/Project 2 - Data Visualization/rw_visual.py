from matplotlib import pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')

fig, ax = plt.subplots(figsize=(15, 10))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')

# Emphasize the first and last points.
ax.scatter(rw.x_values[0], rw.y_values[0], s=100, c='green', edgecolors='none')
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Removing the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()