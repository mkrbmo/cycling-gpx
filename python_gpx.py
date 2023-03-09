import gpxpy
import gpxpy.gpx

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

with open('Day_nine_arcata_.gpx', 'r') as gpx_file:
    gpx = gpxpy.parse(gpx_file)



route_info = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            route_info.append({
                'latitude': point.latitude,
                'longitude': point.longitude,
                'elevation': point.elevation
            })

print(route_info[:3])
route_df = pd.DataFrame(route_info)
route_df.head()

route_df.to_csv('route.df.csv', index=False)