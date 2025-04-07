import geopandas as gpd

# Read the GeoJSON file
gdf = gpd.read_file("data/vt-zoning-expanded-vermont.geojson")

# Split the data into three parts
split_gdfs = [gdf.iloc[i::3] for i in range(3)]

# Save each part as a new GeoJSON file
for i, split_gdf in enumerate(split_gdfs):
    split_gdf.to_file(f"data/vt-zoning-expanded-part{i+1}.geojson", driver="GeoJSON")

print("GeoJSON file has been split into three new files: vt-zoning-update-part1.geojson, vt-zoning-update-part2.geojso")