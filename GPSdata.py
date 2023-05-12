import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx
from pyproj import CRS, Transformer

# Load the data
df = pd.read_excel('GPSdata.xlsx')

# Define the projection for New Jersey State Plane (EPSG:3424)
inProj = CRS('epsg:3424') 
# Define the projection for WGS84 (EPSG:4326)
outProj = CRS('epsg:4326') 

# Transformer
transformer = Transformer.from_crs(inProj, outProj, always_xy=True)

# Apply the transformation
df['longitude'], df['latitude'] = transformer.transform(df['easting'].to_list(), df['northing'].to_list())

# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

# Set the CRS for the GeoDataFrame
gdf.set_crs("EPSG:4326", inplace=True)

# Plot the data
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, column='category', legend=True, alpha=1, markersize=30, marker='s')

# Set x and y labels
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

# Set limits for better zoom
ax.set_xlim([gdf['longitude'].min() - 0.01, gdf['longitude'].max() + 0.01])
ax.set_ylim([gdf['latitude'].min() - 0.01, gdf['latitude'].max() + 0.01])

# Add basemap
ctx.add_basemap(ax, crs=gdf.crs.to_string(), source=ctx.providers.OpenStreetMap.Mapnik)

plt.show()
