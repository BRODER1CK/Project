def count_words(string):
    splitted = string.lower().split()
    dictionary = dict()
    for i in splitted:
        i = i.lower()
        if i.isalpha():
            dictionary[i] = splitted.count(i)
    return dictionary