def curiousQueries(arr, queries):
    results = []

    for query in queries:
        sumToIdx = query[0]
        min = arr[query[1]]
        sum = 0
        for i in range(0, sumToIdx):
            if arr[i] > min:
                sum += arr[i]
        results.append(sum)

    return results


queries = [[2, 2], [3, 1]]

print(curiousQueries([6, 7, 2, 5], queries))
