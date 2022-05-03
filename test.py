a = 100
n = bin(a)
# bin - 10
# oct - 8
# hex - 16


dict = {
    'hex': hex,
    'bin': bin,
    'oct': oct,
}

v = (dict['oct'](a))[2:]

print(v)


s = '11d'.isdigit()

print(s)