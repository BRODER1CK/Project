def sort_list(list):
    if list:
        maximum = max(list)
        minimum = min(list)
        for i in range(len(list)):
            if list[i] == maximum:
                list[i] = minimum
            elif list[i] == minimum:
                list[i] = maximum
        list.append(min(list))
        return list
    else:
        return list