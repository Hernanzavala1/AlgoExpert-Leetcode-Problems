
def findThreeLargestNumbers(array):
    # Write your code here.
    Max = -100000
    secMax = -100000
    thirdMax = -100000  # initialize all 3 variables
    for num in array:
        if num >= Max :
            thirdMax = secMax
            secMax = Max
            Max = num
        elif num >= secMax and num < Max:
            thirdMax = secMax
            secMax = num
        elif num >= thirdMax and num < secMax:
            thirdMax = num

    return [thirdMax, secMax, Max]


print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
