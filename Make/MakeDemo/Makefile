saveFinalOutput: aggregateTask
	python saveFinalOutput.py aggregateTask.txt	
	echo "Pipeline Completed"

aggregateTask: loadFromAPI1 loadFromAPI2 loadFromAPI1.csv loadFromAPI2.csv
	python aggregateTask.py loadFromAPI1.csv loadFromAPI2.csv

loadFromAPI1:
	python loadFromAPI1.py
loadFromAPI2:
	python loadFromAPI2.py
clean:
	rm loadFromAPI1.csv
	rm loadFromAPI2.csv
	rm aggregateTask.txt
	rm saveFinalOutput.txt
