import numpy as np
import pandas as pd

np.random.seed(12345)
data = pd.DataFrame(np.random.randn(1000,4))
print(data.describe())

data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())