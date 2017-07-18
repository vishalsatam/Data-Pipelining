import pandas as pd
import numpy as np
import sys

index=0
filename = False
finavg=[0,0]
for ip in sys.argv:
	with open(ip,"r") as in_file:
		if not filename:
			filename=True
		else:
			users = pd.read_csv(in_file,delimiter=",")
			finavg[index] = np.mean(users.iloc[:,-1])
			index+=1
	with open("aggregateTask.txt","w") as out_file:
	    out_file.write(str(finavg[0]))
	    out_file.write("\n")
	    out_file.write(str(finavg[1]))
