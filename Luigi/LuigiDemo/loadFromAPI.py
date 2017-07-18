import luigi
import pandas as pd
class LoadFromAPI(luigi.Task):
    def run(self):
        query = ("https://data.colorado.gov/resource/ncpu-fd8q.json")
        dd = pd.read_json(query)
        with self.output().open("w") as out_file:
            out_file.write(dd.to_csv())

    def output(self):
        return luigi.LocalTarget("data/loadFromAPI.csv")   