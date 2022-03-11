def sort_list(inList):
    initialList = inList.copy()
    outList = []
    i = 0
    n = len(inList)
    initialList.sort()
    outList = initialList.copy()
    '''
    while i < n:
        firstVal = inList[i]
        checkedIndx = i+1
        while n-i-1 > 0:
            tmpVal = 0
            if (checkedIndx == n):
                break
            else:
                if (firstVal > inList[checkedIndx]):
                    tmpVal = inList[checkedIndx]
                    inList.pop(checkedIndx)
                    outList.insert(0, tmpVal)

                checkedIndx = checkedIndx + 1
        i = i+1
    '''
    return outList

'''
sort_list([3,5,11,8,6])
sort_list(['z','d','c','m','e','a','q','l','o','p','r','t','y','u','n'])
sort_list([5,6,4,654,12,35,456,32,17,35453,323,112313,1568,12315,135348,135646,1218,153,3548,35468,35438,123138,353,35,3,1,9,8,7,10])
sort_list([])
'''
