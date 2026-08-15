def count_sheep(n):
    # your code

    y = ""

    for i in range(0, n):
        count_sheep = i + 1
        y += str(count_sheep) + ' sheep...'

    print(y)

count_sheep(3)
