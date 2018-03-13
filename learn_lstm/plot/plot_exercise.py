# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 19:45:34 2018

@author: hasee
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=pd.DataFrame({'date':pd.date_range('20000101',periods=10),
      'gender':np.random.randint(0,2,size=10),
      'height':np.random.randint(40,50,size=10),
      'weight':np.random.randint(150,180,size=10)})
print(a)

a=pd.DataFrame(np.random.randn(1000,4),index=pd.date_range('20150101',periods=1000),columns=list('ABCD'))
b=a.cumsum()
a.plot()
b.plot()
plt.show()