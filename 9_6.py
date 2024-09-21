import itertools


def all_variants(text):
    for i in range(1, len(text) + 1):
        for combo in itertools.combinations(text, i):
            yield ''.join(combo)


a = all_variants("abc")
for i in a:
    print(i)
