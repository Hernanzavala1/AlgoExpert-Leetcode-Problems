""" def targetSum(array, target):
    start = 0
    end = len(array) - 1 
    currentSum = 0
    result = []
    while(start < end):
        currentSum = array[start] + array[end]
        if(currentSum == target ):
            result.append(array[start])
            result.append(array[end])
            return result
        if(currentSum < target):
            start += 1
        else:
            end -= 1
    return None """
def sum(array, target):
    sum =0
    result = []
    for start in range(len(array)):
        for end in range(start + 1 , len(array)):
            sum = array[start] + array[end]
            if(sum == target):
                result.append(array[start])
                result.append(array[end])
                return result
    return []
def isValidSubsequence(array, sequence):
    # Write your code her
    secIndex =0 
    for number in array:
        if(sequence[secIndex] == number):
            if(secIndex < (len(sequence)-1)):
                secIndex += 1 # we can still continue to look 
            else:
                return True
    return False

def tournamentWinner(competitions, results):
    # Write your code here.
    teamNames= dict()
    for index in range(len(competitions)) :
        lst = competitions[index]
        if(lst[0] not in teamNames):
            teamNames[lst[0]] = 0
        if(lst[1] not in teamNames):
            teamNames[lst[1]] = 0 # add the team  name and initialize them to zero points 
        winningTeam = results[index]
        if(winningTeam == 0):
            teamNames[lst[1] ] = teamNames[lst[1]]+ 3
        else:
            teamNames[lst[0]] = teamNames[lst[0]] + 3
    max = 0
    team = ""
    for k,v in teamNames.items():
        if(v > max):
            max = v
            team = k
    return team


def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    change=0
    for coin in coins:
        if(coin > change + 1):
            return change + 1
        change += coin
    else:
        return change + 1

    return 1


def smallestNegativeBalance(debts):
    # Write your code here
    people = {} #this will hold each person's balance
    result = []
    for i in range(0, len(debts)):
        borrower = debts[i][0]
        lender = debts[i][1]
        if(len(borrower) not in range(1, 21) or len(lender) not in range(1, 21)):
            continue
        amount = int(debts[i][2])
        if(borrower is None or lender is None or amount is None):
            return ["Nobody has a negative balance"]
        if(borrower not in people): # initizialize the person in the dict
            people[borrower] = 0 
        if(lender not in people):
            people[lender] = 0
        people[borrower] -= amount
        people[lender] += amount
    min_val = 0
    for k,v in people.items():
        if v and  v <= min_val:
            min_val = v
            result.append(k)
    if(len(result) == 0):
        return ["Nobody has a negative balance"]
    if(len(result) > 1):
        result.sort()
    return result
            
array  = [['Alex', 'Blake', '5'], ['Blake', 'Alex', "3"], ['Casey', 'Alex', '7'], ['Casey', 'Alex', "4"], ['Casey', 'Alex', '2']]
print(smallestNegativeBalance(array))
def nodeDistance(g_nodes, g_from, g_to):
    # Write your code here
    mergedList = []
    for i in range(0,g_nodes):
        mergedList.append([g_from[i], g_to[i]])
    #print(mergedList)
ar1 = [1,2,1,3,1,2]
ar2 = [2,3,3,5,4,6] 
nodeDistance(6, ar1,ar2)