def find_difference(a, b):
    # Your code here!

    side_a = 1
    side_b = 1

    for i in a:
        side_a *= i

    for i in b:
        side_b *= i

    difference = side_a - side_b if side_a > side_b else side_b - side_a

    print(difference)

find_difference([2, 2, 3], [5, 4, 1])
