# converts an exported QGIS color map to a matplotlib colormap (linear segmented only)

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LinearSegmentedColormap, ListedColormap

with open('colorbar-qgis.txt','r') as intextfile:
    lines = [x.strip().split(',') for x in intextfile.readlines()]

x = []
r = []
g = []
b = []
a = []
for line in lines:
    if len(line) == 6:
        tx,tr,tg,tb,ta,templabel = line;
        x.append(float(tx))
        r.append(float(tr)/255.0)
        g.append(float(tg)/255.0)
        b.append(float(tb)/255.0)
        a.append(float(ta)/255.0)

minx = np.min(x)
maxx = np.max(x)

normx = [(v - minx)/(maxx - minx) for v in x]

cdict = {
           'red':[],
           'green':[],
           'blue':[],
           'alpha':[]
         }

for xval,rval,gval,bval,aval in zip(normx,r,g,b,a):
    cdict['red'].append([xval,rval,rval])
    cdict['green'].append([xval,gval,gval])
    cdict['blue'].append([xval,bval,bval])
    cdict['alpha'].append([xval,aval,aval])

qgis_map = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)

fig,ax = plt.subplots(1,1)
v = np.arange(0,3000.0,5.0)
arr2d = np.repeat([v],50,axis=0)
m = ax.imshow(arr2d,cmap=newcmp)
plt.colorbar(m)
