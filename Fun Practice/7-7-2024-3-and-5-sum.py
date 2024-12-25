import time


def incrementing_by_one():
    sum = 0

    for i in range(1, 1000, 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


start_time = time.time()
print(incrementing_by_one())
end_time = time.time()

print("increment by one:", end_time - start_time)


def two_for_loops():
    sum = 0

    for i in range(3, 1000, 3):
        sum += i

    for i in range(5, 1000, 5):
        if i % 3 != 0:
            sum += i

    return sum


start_time = time.time()
print(two_for_loops())
end_time = time.time()

print("two for loops:", end_time - start_time)
