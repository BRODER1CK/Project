def coincidence(list=None, range=None):
    new_list = []
    if list is None and range is None:
        return new_list
    min_num = range[0] 
    max_num = range[-1]
    for i in list:
        if isinstance(i, int) or isinstance(i, float):
            if min_num <= i <= max_num:
                new_list.append(i)
    return new_list