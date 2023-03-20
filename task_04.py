def sort_list(list):
    if list:
        list[list.index(max(list))], list[list.index(min(list))] = list[list.index(min(list))], list[list.index(max(list))]
        list.append(min(list))
        return list
    else:
        return list