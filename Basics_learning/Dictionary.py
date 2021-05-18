d = dict()
d = {'a': 3, 'x': 2, 'b': 1}

f = d.items()
print(f)

e = sorted(f)
print(e)

for k,v in e:
    print(k,v)
