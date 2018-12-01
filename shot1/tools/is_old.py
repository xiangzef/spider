def is_odd(n, y):
    return n % y == 0


def newlist(list):
    newlist = filter(is_odd, list)
    return newlist

