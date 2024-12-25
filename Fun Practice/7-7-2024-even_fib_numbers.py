def even_fibs():
    fibs = [1, 2]
    sum_evens = 2

    while fibs[len(fibs) - 1] + fibs[len(fibs) - 2] < 4_000_000:

        last = fibs[len(fibs) - 1]
        second_to_last = fibs[len(fibs) - 2]
        next_fib = last + second_to_last

        if next_fib % 2 == 0:
            sum_evens += next_fib

        fibs.append(next_fib)

    return sum_evens


print(even_fibs())
