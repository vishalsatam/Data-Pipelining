import luigi
from loadFromAPI import LoadFromAPI
from loadFromMySQL import LoadFromMySQL
import pandas as pd
import numpy as np

class AggregateTask(luigi.Task):
    
    def requires(self):
        yield LoadFromMySQL()  #incase of two dependencicies, use yieild instead of return
        yield LoadFromAPI()
    
    def run(self):
        finavg = [0,0]
        index = 0
        for ip in self.input():
            with ip.open("r") as in_file:
                users = pd.read_csv(in_file,delimiter=",")
                finavg[index] = np.mean(users.iloc[:,-1])
                index+=1
        with self.output().open("w") as out_file:
            out_file.write(str(finavg[0]))
            out_file.write("\n")
            out_file.write(str(finavg[1]))  
    def output(self):
        return luigi.LocalTarget("data/aggregateOutput.txt")