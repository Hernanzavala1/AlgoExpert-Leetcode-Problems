def minimumWaitingTimme(queries):
    queries.sort()
    waitingTime = [0 for i in range(len(queries))] # the first query will execute immideately
    for i in range(1, len(queries)):
        waitingTime[i] = waitingTime[i-1] + queries[i-1]
    return sum(waitingTime)

print(minimumWaitingTimme([3, 2, 1, 2, 6]))