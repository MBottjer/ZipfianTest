def fileReader(file):
	f = open(file, 'r')
	return f.readlines()

def determineFrequency(arrayOfLines):
	listOfFrequencies = []
	totalPerPosition = []
	for line in arrayOfLines:
		line = line.rstrip('\n')
		for pos in range(len(line)):
			sym = line[pos]
			if pos >= len(listOfFrequencies):
				listOfFrequencies.append({sym: 1})
				totalPerPosition.append(1)
			else:
				if sym in listOfFrequencies[pos].keys():
					listOfFrequencies[pos][sym] += 1
				else:
					listOfFrequencies[pos][sym] = 1
				totalPerPosition[pos] += 1

	return (listOfFrequencies, totalPerPosition)


def calculatePercentages(listOfFrequencies, totalPerPosition):
	count = 0
	for distribution in listOfFrequencies:
		for key in distribution.keys():
			distribution[key] = round(distribution[key] / float(totalPerPosition[count])*100, 1)
		count += 1
	position = 0
	for frequency in listOfFrequencies:
		print "Position: " + str(position) + " " + str(frequency)
		position += 1

(lof, tpp) = determineFrequency(fileReader('example1.txt'))

calculatePercentages(lof, tpp)