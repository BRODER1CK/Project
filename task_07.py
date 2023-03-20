def combine_anagrams(words):
    d = dict()
    for i in words:
        d[''.join(sorted(set(i)))] = d.get(''.join(sorted(set(i))), []) + [i]
    return list(d.values())