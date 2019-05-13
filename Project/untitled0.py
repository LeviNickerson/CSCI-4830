# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 20:28:56 2018

@author: Levi
"""

import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set()

dk = pd.read_csv('D:\School\Summer Semester\CSCI 4830 Special Topics Information Visualization\Project\DKSalaries_8_11_18.csv')

bat = pd.read_csv('D:\School\Summer Semester\CSCI 4830 Special Topics Information Visualization\Project\mlb-player-stats-Batters_8_11_18.csv')

pit = pd.read_csv('D:\School\Summer Semester\CSCI 4830 Special Topics Information Visualization\Project\mlb-player-stats-P_8_11_18.csv' )

top = tk.Tk()

v = tk.IntVar()


radio1 = tk.Radiobutton(top, text="Option 1",variable = v, value = 1).pack()
radio2 = tk.Radiobutton(top, text="1B",value = 2, variable = v).pack()
f = Figure(figsize=(20,10), dpi=100)
a = f.add_subplot(111)



data = []

for i in range(len(dk)):
    
    for j in range(len(bat)):

        if (dk.iloc[i,2] == bat.iloc[j,0]):
            data.append([dk.iloc[i,2], dk.iloc[i,5], bat.iloc[j,2], bat.iloc[j,6]])
        


x = []
y = []
n = []
for k in range(len(data)):
    x.append(data[k][1])
    y.append(data[k][3])
    n.append(data[k][0])


xnew = []
ynew = []
nnew = []

for l in range(len(x)):
        if (data[l][2] == 'C' and data[l][3] > 20):
            xnew.append(data[l][1])
            ynew.append(data[l][3])
            nnew.append(data[l][0])
    


fig, ax = plt.subplots()    
count = 0
markers = ["o","s","*","v","+"]
j = 0
for i in range(len(xnew)):
    if (count == 12):
        j = 1
    if (count == 24):
        j = 2
    if (count == 36):
        j = 3
    if (count == 48):
        j = 4
    
    a.scatter(xnew[i], ynew[i], marker = markers[j], label = nnew[i])
    count = count + 1

a.legend(loc='upper left', prop={'size':10}, bbox_to_anchor=(1,1))

        

canvas = FigureCanvasTkAgg(f, top)
canvas.show()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2TkAgg(canvas, top)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

top.mainloop()