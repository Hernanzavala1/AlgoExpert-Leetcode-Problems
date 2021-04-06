
def smallestSubArray(k, array):
    currentSum = 0
    subArrSize = 1000000
    windowStart = 0
    for windowEnd in range(len(array)):
        currentSum += array[windowEnd]
        while(currentSum >= k):
            subArrSize = min(windowEnd - windowStart  + 1, subArrSize)
            currentSum -= array[windowStart]
            windowStart +=1

    return subArrSize
def maxProfit(prices):
    if(len(prices) < 2):
        return 0
    buyday = 0
    Bprice = prices[buyday]
    lst = [0]
    profit = lst[0]
    for index in range(1,len(prices)):
        if(prices[index] < Bprice and index != (len(prices) - 1)):
            Bprice = prices[index]
            buyday = index
        profit =  max(profit, (prices[index] - Bprice))
        if(profit not in lst):
            lst.append(profit)
                
    return max(lst)
def productExceptSelf(nums):
    result = 1
    zeroP = False
    countZero = 0
    for x in nums:
        if(x != 0):
            result = result * x
        else:
            zeroP = True
            countZero += 1
    if(countZero > 1 ):
        return [0] * len(nums) 
    answer = [] 
    for i in range(len(nums)):
        if(nums[i] == 0):
            answer.append(result)
        elif(zeroP):
            answer.append(0)
        else:
            answer.append((result / nums[i])) # we want to take the nums[i] out of the result
    return answer
def maxSum(nums):
    start=0
    end = 0
    prevMax = [-10000]
    currentMax = prevMax[0]
    currentSum = 0
    if(len(nums) <= 1):
        return nums[0]
    while(end < len(nums) and start < len(nums)):
        currentSum += nums[end] 
        if(currentSum <= prevMax[-1]):
            start = end + 1 
            end +=1
            currentSum = 0
            prevMax.append(currentMax)
            currentMax = -1000
        else:
            currentMax = currentSum
            prevMax.append(currentMax)
            end += 1

    print(prevMax)
    return currentMax

def maxSum2(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i -1] + nums[i], nums[i])
    return max(dp)

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSum2(arr))
