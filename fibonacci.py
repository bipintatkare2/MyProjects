# Project :- Fibonacci Series

def fibonacciNumber(limit):
    first_num, second_num = 0, 1
    if first_num == 0 and second_num == 1:
        print("{} + {} = {}".format(first_num, second_num, first_num+second_num))

    for each in range(limit):

        next_var = first_num+second_num
        first_num = second_num
        second_num = next_var
        print("{} + {} = {}".format(first_num, second_num, first_num+second_num))


num_limit = int(input("Enter No. of times fibonacci series: "))

fibonacciNumber(num_limit)