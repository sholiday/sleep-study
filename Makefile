all: data/notes.txt

data/minutesAsleep.sv:
	python bin/download_fitbit_minutesAsleep > data/minutesAsleep.csv

data/notes.txt: data/collection.anki2
	python bin/extract_cards.py data/collection.anki2 > data/cards.json

data/collection.anki2:
	unzip data/LS101.apkg collection.anki2 -d data