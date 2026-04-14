def mortal_fibonacci(n, m):
    """
    Calculate number of rabbit pairs after n months with lifespan m.

    Args:
        n: number of months to simulate
        m: lifespan of each rabbit pair in months

    Returns:
        total number of rabbit pairs alive after month n
    """
    # rabbits[0] = pairs of age 1 (newborns)
    # rabbits[1] = pairs of age 2 (first reproduction)
    # rabbits[m-1] = pairs of age m (die next month)
    rabbits = [0] * m
    rabbits[0] = 1  # start with one newborn pair in month 1

    for month in range(2, n + 1):
        # only mature pairs reproduce (age 2 and older = index 1 and up)
        new_births = sum(rabbits[1:])

        # shift everyone one age forward, drop the oldest (they die)
        # rabbits[:-1] removes the last element (oldest group)
        rabbits = [new_births] + rabbits[:-1]

    return sum(rabbits)


def main():
    with open("rosalind_fibd.txt") as f:
        n, m = map(int, f.read().split())

    result = mortal_fibonacci(n, m)
    print(result)


if __name__ == "__main__":
    main()
