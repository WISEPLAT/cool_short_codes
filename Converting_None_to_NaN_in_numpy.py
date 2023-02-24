# Converting None to NaN in numpy when casting a list to numpy arrays #numpy #python
import numpy as np

x = array([3,4,None,55])

y = np.array(x,dtype=float)

# OR

y = np.array(x)
z = y.astype(float)
