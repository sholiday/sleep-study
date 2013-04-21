import fitbit
import json
import csv

keys = json.load(open('keys.json'))
c = fitbit.Fitbit(keys['consumer_key'], keys['consumer_secret'],
									user_key=keys['user_key'], user_secret=keys['user_secret'])

#metrics = ['minutesAsleep']
metrics = ['startTime', 'timeInBed', 'awakeningsCount', 'minutesAsleep',
					 'minutesAwake', 'minutesToFallAsleep', 'minutesAfterWakeup',
					 'efficiency']

sleep = dict()

for metric in metrics:
	for r in c.time_series('sleep/'+metric, period='max')['sleep-'+metric]:
		if r['dateTime'] not in sleep:
			sleep[r['dateTime']] = dict()
		sleep[r['dateTime']][metric]=r['value']

rows = list()

for k in sleep:
	#print k
	#print sleep[k]
	v=sleep[k]
	if True: #int(v['minutesAsleep']) > 0:
		row = list()

		row.append(k)
		for metric in metrics:
			row.append(v[metric])

		rows.append(row)

rows = sorted(rows, key=lambda r: r[0])

ofile = open('data/sleep.csv', 'wb')
writer = csv.writer(ofile, dialect='excel')

writer.writerow(['Date']+metrics)
for row in rows:
	writer.writerow(row)