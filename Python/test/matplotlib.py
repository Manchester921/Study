#-*- coding:utf-8 -*-
"""
    matplotlib.py
    ~~~~~~~~~~~~~~~~~
    matplotlib可视化绘图
"""


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.2)
y = np.cos(x)

plt.polt(x,y,'r-')
