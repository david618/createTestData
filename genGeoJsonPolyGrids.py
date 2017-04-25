import json
import os

#folder = r"/home/david/Documents/Test"
folder = ""

fout = open(os.path.join(folder, "grids.json"), "w")

obj = {}
obj['type'] = "FeatureCollection"

features = []

for lon in range(-180,180):        
    
    for lat in range(-90,90):
        
        feature = {}

        feature['type'] = "Feature"

        props = {}
        props['lon'] = lon
        props['lat'] = lat

        feature['properties'] = props         

        geom = {}
        geom['type'] = "Polygon"

        rings = []
        coords = []
        pt = []
        pt.append(lon)
        pt.append(lat)
        coords.append(pt)

        pt = []
        pt.append(lon + 1)
        pt.append(lat)
        coords.append(pt)

        pt = []
        pt.append(lon + 1)
        pt.append(lat + 1)
        coords.append(pt)
        
        pt = []
        pt.append(lon)
        pt.append(lat + 1)
        coords.append(pt)
        
        pt = []
        pt.append(lon)
        pt.append(lat)
        coords.append(pt)

        rings.append(coords)
        
        geom['coordinates'] = rings

        feature['geometry'] = geom

        features.append(feature)


obj['features'] = features

jsonStr = json.dump(obj, fout)
fout.close()
