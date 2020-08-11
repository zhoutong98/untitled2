import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.rand(10, 4), index= list("ABCDE"),columns= list("xy"))
data.plot.pie(subplots= True, figsize= (8, 4));