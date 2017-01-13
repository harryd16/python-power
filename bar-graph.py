from matplotlib import pyplot as plot
import numpy

animals = ['Dog', 'Cat', 'Zebra', 'Lion']
counts = [20, 32, 12, 18]

y_pos = numpy.arange(len(animals))

plot.barh(y_pos, counts, align='center')
plot.yticks(y_pos, animals)

plot.show()
