import luigi
import numpy as np
from aggregateTask import AggregateTask

class SaveFinalOutput(luigi.Task):
    
    def requires(self):
        return AggregateTask()
    
    def run(self):
        sm=0
        with self.input().open("r") as in_file:
            arr = np.loadtxt(in_file)
            sm = np.sum(arr)
        with self.output().open("w") as out_file:
            out_file.write(str(sm)) 
    def output(self):
        return luigi.LocalTarget("data/saveFinalOutput.txt")