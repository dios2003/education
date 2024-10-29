# Домашнее задание по теме "Генераторы"


def all_variants(text):
    for e in range(len(text)):
        for s in range(len(text)-e):
            yield text[s:s+e+1]


a = all_variants("abc")
for i in a:
    print(i)
