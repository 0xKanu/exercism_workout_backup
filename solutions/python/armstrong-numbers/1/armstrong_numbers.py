def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)

    total_sum = sum(int(num)** num_digits for num in num_str)

    return number == total_sum
