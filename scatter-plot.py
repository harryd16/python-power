from matplotlib import pyplot as plot
import numpy

# Magnetic poles or something
distance = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
field_strength = [55.66, 23.35, 11.07, 6.37, 3.63, 2.72, 1.87, 1.45, 1.09, 0.87]

#plot.scatter(distance, field_strength)
#plot.xlabel("Distance from South Pole (cm)")
#plot.ylabel("Magnetic Field Strength (G)")
#plot.title("Field Strengths at varying distances from Magnetic Pole")

#plot.show()

#plot.clf()

# Field strength due to change in voltage

voltage = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
magnetic_field_strength = [0.00, 12.14, 24.29, 36.43, 48.57, 60.72, 72.86, 85.00, 97.15, 109.29, 121.43]
print(len(voltage), len(magnetic_field_strength))
plot.title("Field strength due to change in voltage")
plot.scatter(voltage, magnetic_field_strength)

#plot.show()
#plot.clf()

# Line of Best Fit
model = numpy.polyfit(voltage, magnetic_field_strength, 1)
lobf = numpy.poly1d(model)
plot.title("Line of Best Fit")

plot.plot(lobf(voltage))

plot.show()
