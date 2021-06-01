def calc_lucky_tickets_count(n):
    return next(n)


def next(n, nextN=0, count=0, sum1=0, sum2=0):
    if n * 2 == nextN:
        if (sum1 == sum2):
            count += 1

        return count

    for i in range(10):
        if nextN < n:
            count = next(n, nextN + 1, count, sum1 + i, sum2)
        else:
            count = next(n, nextN + 1, count, sum1, sum2 + i)

    return count


print(calc_lucky_tickets_count(3))
