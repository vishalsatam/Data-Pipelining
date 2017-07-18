import pandas as pd
query = ("https://data.colorado.gov/resource/ncpu-fd8q.json")
dd = pd.read_json(query)
with open("loadFromAPI1.csv","w") as out_file:
    out_file.write(dd.to_csv()) 
