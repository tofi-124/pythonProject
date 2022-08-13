from datetime import date


def converter(inp):
    if type(inp) == str:
        inp = int(inp)
    else:
        inp = str(inp)

    return inp


birth_year = input('What year was you born in: ')

date = converter(date.today())

cur_year = date[:4]

try:
    old = converter(converter(cur_year) - converter(birth_year))
    print('You are ' + old + ' years old.')
except ValueError:
    print('Value is not an int or str')


