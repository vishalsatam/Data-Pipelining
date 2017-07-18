import pandas as pd
query = ("https://data.colorado.gov/resource/ujff-j2yj.json")
dd = pd.read_json(query)
with open("loadFromAPI2.csv","w") as out_file:
    out_file.write(dd.to_csv()) 
