abc = {'zero':0,'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

# set deafult rows to 6 items
r1 = [abc[4], abc[5], abc[6], abc[2], abc[1], abc[3]]
r2 = [abc[3], abc[1], abc[2], abc[5], abc[4], abc[6]]
r3 = [abc[5], abc[4], abc[3], abc[1], abc[6], abc[2]]
r4 = [abc[6], abc[2], abc[1], abc[3], abc[5], abc[4]]
r5 = [abc[2], abc[6], abc[5], abc[4], abc[3], abc[1]]
r6 = [abc[1], abc[3], abc[4], abc[5], abc[2], abc[5]]

# tuple of rows
rows = (r1, r2, r3, r4, r5, r6)
