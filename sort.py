print("Input numbers for list: ")

def sort_list(inList):
    print(f'Input list: {inList}')
    i = 0
    n = len(inList)
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
                    inList.insert(i, tmpVal)

                checkedIndx = checkedIndx + 1
        i = i+1
    print(inList)

sort_list(list(input()))
