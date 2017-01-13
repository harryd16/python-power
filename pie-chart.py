from matplotlib import pyplot as plot
import numpy

animals = ["Moose", "Giraffe", "Beaver", "Stingray", "Elephant", "Penguin"]
counts = [3, 2, 3, 3, 2, 8]

plot.axis("equal")
colors = ["yellowgreen", "gold", "lightskyblue", "lightcoral"]
explode = [0, 0, 0, 0, 0, 0.1]
plot.pie(counts, labels=animals, shadow=True, autopct="%1.1f%%", colors=colors, explode=explode)

plot.show()
