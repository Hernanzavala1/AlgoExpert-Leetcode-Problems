def climbStairs(n):

    if(n == 1):
        return 1
    if(n == 2):
        return 2
    result = climbStairs(n - 1) + climbStairs(n - 2)
    return result
def climbStairs2(n):
    if(n ==1 or n == 2):
        return n
    arr = [1,2]
    for i in range(2, n + 1):
        arr.append((arr[i - 1] + arr[i - 2 ]))
    return arr[n - 1] # index issues

def getNthFib(n):
	result = [0, 1]
	for i in range(2,n):
		result.append((result[i - 1] + result[i -2]))
    return result[-1]
getNthFib(6)