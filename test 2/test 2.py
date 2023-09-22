import numpy as np

#permet de réarranger une array par colonne puis par ligne
a = np.arange(15).reshape(3, 5)
"""print(a)"""

#permet de savoir la forme ( colonne puis ligne) d'une array
s=a.shape
"""print(s)"""

#permet de savoir le nombre d'axes dans une array
h=a.ndim
"""print(h)"""

#determine les types selon une valeur qui lui est propre( numpy.int32, numpy.int16, and numpy.float64)
h=a.dtype.name
"""print(h)"""

#permet de savoir la taille en octet
h=a.itemsize
"""print(h)"""

#permet de savoir le nombre d'objet dans une array
h=a.size
""""print(h)"""


b = np.array([6, 7, 8])
print(b)
h=type(b)
print(h)