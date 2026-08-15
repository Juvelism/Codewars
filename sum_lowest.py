def sum_two_smallest_numbers(numbers):

    num1 = min(numbers)
    numbers.remove(num1)
    num2 = min(numbers)

    print(num1 + num2)


    print(type(num2))
sum_two_smallest_numbers([19, 5, 42, 2, 77])
