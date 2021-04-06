def sockMerchant(n, ar):
    hashColors ={}
    numPairs = 0
    for index in range(0, n):
        if(ar[index] not in hashColors):
            hashColors[ar[index]] = 1
        else:
            hashColors[ar[index]] += 1
 
        if(hashColors[ar[index]]  % 2 ==0):
            numPairs +=1
    return numPairs

def countingValleys(steps, path):
    currentAltitude = 0 # sea level will be 0 anything below is valley
    numberOfValleys = 0
    inValley = False
    
    for index in range(0, steps ):
        if(path[index] == 'D'):
            currentAltitude -=1
            if(currentAltitude < 0 ):
                inValley = True
        elif(path[index] == 'U'):
            currentAltitude +=1
            if(currentAltitude == 0):
                inValley = False
                numberOfValleys +=1
    return numberOfValleys
def rotLeft(a, d):
    result = []
    shiftVal = len(a) - d
    arrayLen = len(a)
    for i in range(0, len(a)):
        newIndex = ((i + shiftVal) % arrayLen)
        print(newIndex)
        result.insert(newIndex, a[i])
    return result

def intersect( nums1, nums2):
    counter = 0
    result = []
    inBoth = {}
    while(counter < len(nums1) and counter < len(nums2)):
        if(nums1[counter] == nums2[counter]):
            if(nums1[counter] not in inBoth):
                inBoth[nums1[counter]] = 1
            else:
                inBoth[nums1[counter]] += 1
        counter += 1
    print(inBoth) 
    for key,value in inBoth.items():
        result += ([key] * value)
    return result
print(intersect([4,9,5], [9,4,9,8,4]))
