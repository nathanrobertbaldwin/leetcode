cache = {}


def handleQueries(arr, queries):
    for query in queries:
        return curiousQueries(arr, query)


def curiousQueries(arr, query):
    sumToIdx = query[0]
    minimum = arr[query[1]]
    if minimum in cache:
        prevSummedTo = len(cache[minimum]) - 1
        if prevSummedTo < len(cache[minimum]) - 1:
            priorSum = cache[minimum][prevSummedTo]
            for i in range(prevSummedTo + 1, sumToIdx + 1):
                if arr[i] > minimum:
                    priorSum += arr[i]
                    cache[minimum].append(priorSum)
                else:
                    cache[minimum].append(priorSum)
            return cache[minimum][sumToIdx]
    else:
        cache[minimum] = []
        sum = 0
        for i in range(0, sumToIdx + 1):
            if arr[i] > minimum:
                sum += arr[i]
                cache[minimum].append(sum)
            else:
                cache[minimum].append(sum)

        return cache[minimum][sumToIdx]


print(handleQueries([6, 7, 2, 5, 9, 3, 4, 10, 1], [[3, 3], [5, 3], [8, 4]]))
