import sys
import numpy as np
with open(sys.argv[1],"r") as in_file:
	arr = np.loadtxt(in_file)
	sm = np.sum(arr)
	with open("saveFinalOutput.txt","w") as out_file:
		out_file.write(str(sm))
