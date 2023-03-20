def connect_dicts(dict1, dict2):
    total1 = 0
    total2 = 0
    new_dict = dict()
    for i in dict1.values():
        total1 += i
    for i in dict2.values():
        total2 += i
    if total1 > total2:
        for k, v in dict2.items():
            if v > 10:
                new_dict[k] = v
        for k, v in dict1.items():
            if v > 10:
                new_dict[k] = v
    else:
        for k, v in dict1.items():
            if v > 10:
                new_dict[k] = v
        for k, v in dict2.items():
            if v > 10:
                new_dict[k] = v
    return dict(sorted(new_dict.items(), reverse=True))