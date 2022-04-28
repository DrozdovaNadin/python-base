# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь
# в котором ключи — первые буквы имен, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
#
# def thesaurus(*args):


def thesaurus(*args):
    b = {}
    for ln in args:
        if ln[0] in b:
            b[ln[0]] = b[ln[0]] + ', ' + ln
        else:
            b[ln[0]] = ln
    # return b
    c = {}
    for k, v in b.items():
        # k in sorted(b.keys())
        c[k] = v.split()
        # r = ("{0}: {1}".format(k, v))
    m = {}
    for key in sorted(c.keys()):
        m[key] = c[key]
    return m


print(thesaurus('Мария', 'Юрий', 'Анатолий', 'Анна', 'София', 'Надежда', 'Матвей', 'Луиза'))

# thesaurus('Ольга', 'Михаил', 'Анастасия', 'Олеся', 'Антон')



