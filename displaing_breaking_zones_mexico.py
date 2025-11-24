import fastf1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.collections import LineCollection


quali_mexico = fastf1.get_session(2025, 'Mexico', 'Q')
quali_mexico.load(laps =True, telemetry=True)

lap = quali_mexico.laps.pick_driver('HAM').pick_fastest()

x = lap.telemetry['X']            
y = lap.telemetry['Y']            

color = lap.telemetry['nGear']


points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)



fig, ax = plt.subplots(sharex=True, sharey=True, figsize=(12, 6))
fig.set_facecolor("#FFFFFF")
ax.set_facecolor("#FFFFFF")
ax.set_aspect('equal')

ax.plot(lap.telemetry['X'], lap.telemetry['Y'],
        color='black', linestyle='-', linewidth=16, zorder=0)
lc = LineCollection(segments, cmap=plt.cm.viridis, norm=plt.Normalize(1, max(color)))

lc.set_array(color)
lc.set_linewidth(5)
ax.add_collection(lc)
plt.suptitle(f"HAM Fastest Lap Onboard Telemetry - Gears\n" 
             f"{quali_mexico.event.year} {quali_mexico.event.EventName} Grand Prix", size=20, color='#000000')

cbar = fig.colorbar(lc, ax=ax, label="Gear") 
cbar.set_label("Gear", color='#000000') 
cbar.ax.tick_params(colors='#000000')

ax.set_xlabel("X", color='#000000')
ax.set_ylabel("Y", color='#000000')


plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
plt.show()
