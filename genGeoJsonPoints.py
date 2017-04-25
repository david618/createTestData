import json
import os

folder = r"D:\Temp\dataPnts"



start = 30.0
end = 50.0

rng = 100
diff = (end - start)/rng

print diff


for i in range(0,rng):

    fout = open(os.path.join(folder, "file" + str(i) + ".json"), "w")

    obj = {}

    obj['type'] = "FeatureCollection"

    features = []
    
    lon = start + diff*i
    
    for j in range(0,rng):

        lat = start + diff*j
        
        feature = {}

        feature['type'] = "Feature"

        props = {}
        props['id'] = i * rng + j


        feature['properties'] = props 
        

        geom = {}
        geom['type'] = "Point"


        pt = []
        pt.append(lon + diff/2)
        pt.append(lat + diff/2)
        
        
        geom['coordinates'] = pt

        feature['geometry'] = geom

        features.append(feature)


    obj['features'] = features

    jsonStr = json.dump(obj, fout)
    fout.close()
