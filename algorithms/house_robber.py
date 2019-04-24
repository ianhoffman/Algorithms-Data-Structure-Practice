def house_robber(houses):
    a, b = 0, 0
    for val in houses:
        b, a = max(val + a, b), b
    return b


if __name__ == '__main__':
    assert house_robber([3, 10, 3, 1, 2]) == 12
