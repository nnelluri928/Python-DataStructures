
def quickSort(listToSort,lowIndex,highIndex):
    if (highIndex-lowIndex) > 0:
        p = partition(listToSort,lowIndex,highIndex)
        quickSort(listToSort,lowIndex,p-1)
        quickSort(listToSort,p+1,highIndex)

def partition(listToSort,lowIndex,highIndex):
    divider =lowIndex
    pivot = highIndex

    for i in range(lowIndex,highIndex):
        if listToSort[i] < listToSort[pivot]:
            listToSort[i],listToSort[divider] = listToSort[divider],listToSort[i]
            divider += 1
    listToSort[divider],listToSort[pivot] = listToSort[pivot],listToSort[divider]
    return divider
testList1 = [7, 4, 1, 9, 6, 0, 2, 8, 3, 5]
quickSort(testList1,0,len(testList1)-1)
print(testList1)
testList2=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
quickSort(testList1,0,len(testList1)-1)
print(testList1)