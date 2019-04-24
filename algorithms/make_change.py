import sys


def make_change(denominations, amount):
    cache = {}

    def subproblem(i, remaining_amount):
        if (i, remaining_amount) in cache:
            return cache[(i, remaining_amount)]
        else:
            if i >= len(denominations) or remaining_amount < 0:
                n_coins = sys.maxsize
            elif remaining_amount == 0:
                n_coins = 0
            else:
                n_coins = min(
                    subproblem(i, remaining_amount - denominations[i]) + 1,
                    subproblem(i + 1, remaining_amount)
                )

            cache[(i, remaining_amount)] = n_coins
            return n_coins

    return subproblem(0, amount)


if __name__ == '__main__':
    print(make_change([21, 8, 1], 88))

