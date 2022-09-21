import numpy as np
x = np.array([[1,2,3], [4,5,6]])
print("x:\n{}".format(x))

import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker="x")
plt.show()


import pandas as pd
from IPython.display import display
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        "Location": ["New York", "Paris", "Berlin", "London"],
        "Age": [24, 13, 53, 33]}
data_pandas = pd.DataFrame(data) #dataframe makes data into pandas table
display(data_pandas)

display(data_pandas[data_pandas.Age > 30])
display(data_pandas[data_pandas.Location > "M"])