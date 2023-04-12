from string import punctuation
def count_words(string):
    splitted = ''.join(filter(lambda x: x.isalpha() or x.isspace(), string.lower())).split()
    dictionary = {i: splitted.count(i) for i in splitted}
    return dictionary