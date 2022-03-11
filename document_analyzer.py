def wordCounter(doc):
    wordList = ""
    if doc is str:
        wordList = doc.replace(",", "").replace(".", "").split()
    else:
        return False
    wordDict = {}
    for i in wordList:
        if bool(wordDict) == True:
            keyList = []
            keyList.extend(wordDict.keys())
            for n in keyList:
                if i == n:
                    wordDict[n] = wordDict.get(n) + 1
                    break
                elif n == keyList[-1]:
                    wordDict.update({i: 1})
        else:
            wordDict.update({i: 1})
    return format(wordDict)

def format(dictions):
    topFive = []
    key = []
    vals = []
    key.extend(dictions.keys())
    vals.extend(dictions.values())
    while vals is not False:
        lrgest = vals[0]
        cmpval = None
        if len(topFive) == 5:
            break
        for indx in vals:
            if cmpval is None and lrgest is not indx:
                cmpval = indx
            elif cmpval is not None and cmpval > lrgest:
                lrgest = cmpval
                cmpval = None
            topFive.append(f"{key[vals.index(lrgest)]}: {vals[vals.index(lrgest)]}")
            key.pop(vals.index(lrgest))
            vals.pop(vals.index(lrgest))
    print()
    for fiver in topFive:
        print(fiver)
