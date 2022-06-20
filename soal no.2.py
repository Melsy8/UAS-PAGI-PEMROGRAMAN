y = 5
x = 2 * y - 2
for i in range(0, y):
    for j in range(0, x):
        print(' ', end='')
    x -= 2
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
