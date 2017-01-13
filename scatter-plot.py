from matplotlib import pyplot as plot
import numpy

distance = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
field_strength = [55.66, 23.35, 11.07, 6.37, 3.63, 2.72, 1.87, 1.45, 1.09, 0.87]

plot.scatter(distance, field_strength)
plot.show()
