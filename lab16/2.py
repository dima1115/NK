import pylab
import numpy as np

spis={'Mercedes':60000, 'Audi':55000, 'BMW':75000,'Porshe':90000}
x=np.array(list(spis.keys()))
y=np.array(list(spis.values()))
pylab.bar (x, y)
pylab.show()