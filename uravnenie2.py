for n in range(0, 100):
    for k in range(0, 100):
        for m in range(0, 100):
            if 10 * n + 5 * m + 0.5 * k == 100 and n + m + k == 100:
                print('n = ', n, 'k = ', k, 'm = ', m)
