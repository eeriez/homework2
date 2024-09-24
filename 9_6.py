def all_variants(text):
    for i in range(1, len(text) + 1):
        for j in range(0, len(text) - i + 1):
            result = text[j:(j + i)]
            yield result


a = all_variants("abc")
for i in a:
    print(i)
