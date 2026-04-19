# this code print a pattern of 0-9 rows and 0-9 column

for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end = '')
    print()
