import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2*np.pi,2*np.pi,100)
y = np.sinc(x)

fig,ax = plt.subplots(ncols=4,figsize=(24,8))
ax[0].plot(x,y)
ax[0].set_title('pojedyncza krzywa')

ax[1].plot(x,y)
ax[1].plot(x*2.0,y)
ax[1].set_title('dwie krzywe - I')

ax[2].plot(x,y)
ax[2].set_title('pojedyncza krzywa')

ax[3].plot(x,y)
ax[3].plot(x*1.5,y*1.5)
# ax[3].relim()
# ax[3].autoscale_view()
ax[3].set_title('dwie krzywe - II')

plt.show()
