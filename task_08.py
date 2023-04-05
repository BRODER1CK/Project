def multiply_numbers(inputs=None):
    total = 1
    if inputs is None:
        return None
    for i in str(inputs):
        if i.isdigit():
            total *= int(i)
    if total != 1:
       return total
    else:
        return None