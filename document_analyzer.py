def wordCounter(doc):
    wordList = doc.replace(",", "").replace(".", "").split()

    for i in wordList:
	if bool(wordList) == True:
	    keyList = []
	    keyList.extend(wordList.keys())
	    for n in keyList:
		if i == n:
		    wordList[n] = wordList.get(n) + 1
		    break
		elif n == keyList[-1]:
        	    wordList.update({i: 1})
		else:
		    wordList.update({i: 1})
    print()

shortString("This is a reletively short string with no repeats.")
