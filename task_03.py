def max_odd(list):
    maximum = 0
    for i in list:
        if (isinstance(i, int) or isinstance(i, float)) and i % 2 == 1 and i > maximum:
            maximum = int(i)
    if maximum != 0:
        return maximum
    else:
        return None