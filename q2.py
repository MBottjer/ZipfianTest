import string
import sys

# paragraph = "This is an example of why you shouldn't use an example paragrpah. This is another example. Perhaps I should? Isn't this correct? This is correct!"

def totalWordCount(paragraphs):
	count = 0
	for word in paragraphs.split():
		count += 1
	return count

def uniqueWords(paragraphs):
	frequency = {}
	paragraphs = paragraphs.translate(None, string.punctuation).lower()
	for word in paragraphs.split():
		if word in frequency:
			frequency[word] += 1
		else:
			frequency[word] = 1
	return frequency

def numberOfSentences(paragraphs):
	return paragraphs.count('.') + paragraphs.count('?') + paragraphs.count('!')

def averageSentenceLength(paragraphs):
	sentencesArray = paragraphs.replace("?", ".").replace("!", ".").split(".")
	count = 0
	for array in sentencesArray:
		count += len(array.split())
	
	return count / float(len(sentencesArray) - 1)

def readFromTerminal():
	return "".join(map(lambda S: S.rstrip('\n'), sys.stdin.readlines()))

paragraph = readFromTerminal()

frequency = uniqueWords(paragraph)

print "Total Word count: " + str(totalWordCount(paragraph))
print "Unique words: " + str(len(frequency))
print "Sentences: " + str(numberOfSentences(paragraph))
print "Average Sentence Length: " + str(averageSentenceLength(paragraph))
print "Descending frequency: " + str(map(lambda val: val[0], sorted(frequency.items(), key=lambda val: val[1], reverse=True)))
