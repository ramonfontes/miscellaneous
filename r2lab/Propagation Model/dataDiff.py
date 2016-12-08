#!/usr/bin/env python

import matplotlib.ticker as tick
from matplotlib.ticker import ScalarFormatter
from matplotlib.ticker import FormatStrFormatter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np 
import glob
from pylab import *
from operator import itemgetter, attrgetter, methodcaller
import matplotlib.ticker as ticker
import math

f1 = open('./mininet.diff', 'r')
f2 = open('./data.r2lab.diff', 'r')
f3 = open('./itu.diff', 'r')
f4 = open('./ituPL32', 'r')

file_f1 = f1.readlines()
file_f2 = f2.readlines()
file_f3 = f3.readlines()
file_f4 = f4.readlines()

f1.close()
f2.close()
f3.close()
f4.close()

# initialize some variable to be lists:
f1l0 = []
f1l1 = []
f1l2 = []
f1l3 = []

f2l1 = []
f2l2 = []
f4l1 = []

t=-17.54
z=-8.764

# scan the rows of the file stored in lines, and put the values into some variables:
for newline in file_f1:	
    p = newline.split()
    f1l0.append(float(p[0]))
    f1l1.append(float(p[1]))
    f1l2.append(float(p[2]))
    f1l3.append(float(p[3]))

for newline in file_f2:	
    p = newline.split()
    f2l1.append(float(p[0]))
    f2l2.append(float(p[1]))

key = 0
i = 0
dic = dict()
aa = dict()
dic.setdefault(key, [])
aa.setdefault(key, [])

for newline in file_f3:	
    i += 1
    p = newline.split()
    dic[key].append(float(p[1]))
    if len(dic[key]) >= 2:
        di = (float(dic[key][len(dic[key])-1]) - dic[key][len(dic[key])-2])
        if len(dic[key]) == 2:
            aa[key].append(float(di))
	elif len(dic[key]) > 2:  
            aa[key].append(float(di + aa[key][len(aa[key])-1]))  
    if i % 7 == 0:
        key += 1
        if key < 20:
            dic.setdefault(key, [])
            aa.setdefault(key, [])

for newline in file_f4:	
    p = newline.split()
    f4l1.append(float(p[0]))

fig, ax1 = plt.subplots()
ax1.grid(True)

o = []
for k in f1l0: 
    o.append(t*math.log10(k)+z)

print o

ax1.plot(f2l1, f2l2, color='black', linestyle='-', label='R2Lab Testbed', markevery=7, linewidth=2)
ax1.plot(f1l0, f1l1, color='red', linestyle='--', label='Mininet-WiFi (Free-Space)', markevery=7, linewidth=2)
ax1.plot(f1l0, f1l2, color='blue', linestyle=':', label='Mininet-WiFi (Log-Distance)', markevery=7, linewidth=2)
ax1.plot(f1l0, f4l1, color='green', linestyle='-.', label='Mininet-WiFi (ITU)', markevery=7, linewidth=2)

ax1.legend(loc='best', borderaxespad=0., fontsize=12, frameon=False)
ax1.set_xscale("log", nonposx='clip')
plt.tick_params(axis='x', which='minor')

y_fmt = tick.FormatStrFormatter('%d')
ax1.xaxis.set_major_formatter(y_fmt)

ax1.xaxis.set_minor_formatter(tick.FormatStrFormatter('%d'))

ax1.set_ylabel("dBm", fontsize=20)
ax1.set_xlabel("log(distance) - meters", fontsize=20)
plt.savefig("propagationRSSI.eps")
plt.clf()
