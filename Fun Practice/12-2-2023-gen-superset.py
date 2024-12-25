def genSuperSet(arr, height=0, superSet=[]):
    if height == arr.length:
        return superSet
    else:
        genSuperSet(arr, height + 1, [])


print(genSuperSet([1, 2, 3, 4]))
