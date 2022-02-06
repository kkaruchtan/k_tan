# file_name.py
# -*- coding: utf-8 -*-
# Python3.6
"""
Created on Wed Mar 27 08:28:05 2019

@author: kristianriebesel
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

data_hiv=np.loadtxt("HIVseries.csv",delimiter=',')
N=np.size(data_hiv,0)
x=data_hiv[0:N:1,0]
y=data_hiv[0:N:1,1]

ax=plt.figure(1).add_subplot(1,1,1)

plt.title("HIV Serie", size=18, weight='bold')
ax.set_xlabel("Infektion")
plt.ylabel("Rate")

plt.xlim(0,10)
plt.ylim(0,190000)

plt.plot(x,y,'b--o')

