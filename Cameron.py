abc = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

# set deafult rows to 6 items
r1 = [abc['d'], abc['e'], abc['f'], abc['b'], abc['a'], abc['c']]
r2 = [abc['c'], abc['a'], abc['b'], abc['e'], abc['d'], abc['f']]
r3 = [abc['e'], abc['d'], abc['c'], abc['a'], abc['f'], abc['b']]
r4 = [abc['f'], abc['b'], abc['a'], abc['c'], abc['d'], abc['d']]
r5 = [abc['b'], abc['f'], abc['e'], abc['d'], abc['c'], abc['a']]
r6 = [abc['a'], abc['c'], abc['d'], abc['f'], abc['b'], abc['e']]

# tuple of rows
rows = (r1, r2, r3, r4, r5, r6)
