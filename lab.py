#!/usr/bin/env python
# -*- coding: utf-8 -*-

FILENAME = 'data.csv'
user = '915642913' 


def parse(fileName):
	f = open(fileName, 'r')
	result = []
	for line in f:
		result.append(line.strip().split(','))
	f.close()			
	return result

def charge(data):
	incoming = 1
	outcoming = 1

	if (len(data) < 2):
		print('No data')
		return 0

	price = 0

	columns = []

	for a in data[0]:
		columns.append(a)

	for line in data[1:]:
		origin = False
		dest = False
		for a in range(len(columns)):
			if (columns[a] == 'msisdn_origin' and line[a] == user):
				origin = True
			elif (columns[a] == 'msisdn_dest' and line[a] == user):
				dest = True
			elif (columns[a] == 'call_duration' and (dest or origin)):
				if (dest):
					price += outcoming*float(line[a])
				elif (origin):
					price += incoming*float(line[a])
			elif (columns[a] == 'sms_number' and origin):
				if (float(line[a]) > 5):
					if (float(line[a]) > 10):
						pay = 5 + (float(line[a])-10)*2
					else:
						pay = float(line[a]) - 5
					price += pay

	return price

result = charge(parse(FILENAME))
output = open('output.txt', 'w')
output.write('Price: ' + str(result) + '\n')
output.close()


