def numWaterBottles(numBottles, numExchange):
    drink = numBottles

    while numBottles >= numExchange:
        fullBottles = numBottles // numExchange
        emptyBottles = numBottles % numExchange
        drink += fullBottles
        numBottles = fullBottles + emptyBottles

    return drink


print(numWaterBottles(9, 3))
