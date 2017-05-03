import string

book = open("dracula.txt").read().split()
book = [word.strip("._,!?()\'\"").lower() for word in book]


def frequencyOf(word):
	return len(filter(lambda x: x == word.lower(), book))

def totalFrequencyOf(words):
	words = map(lambda x: frequencyOf(x.lower()),words)
	return reduce(lambda a,b: a + b, words)


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))

def mostCommon():
	words = list(set(book[:500]))
	

	#track current top
	highest = {"word":"","frequency":0}
	#counter = 1
	for word in words:
		x = frequencyOf(word)
		if  x > highest["frequency"]:
			highest["frequency"] = x
			highest["word"] = word
			
		#print counter
		#counter+=1
	return highest

print "frequencies"
print ("the",frequencyOf("the"))
print ("he",frequencyOf("he")) 
print ("dracula",frequencyOf("dracula"))

print(totalFrequencyOf(["the","he"]))

print("most common word",mostCommon())



