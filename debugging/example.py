import ipdb
import other_functions as of


def sum(a,b):
    return a+b

def sort_numbers(numbers):
    ipdb.set_trace()
    sorted_numbers = sorted(numbers, reverse=True)
    k = sum(sorted_numbers[0],sorted_numbers[-1])
    kk = of.resta(sorted_numbers[1],sorted_numbers[4])
    return sorted_numbers


def main():
    numbers = [5, 2, 8, 1, 9, 4]
    sorted_numbers = sort_numbers(numbers)
    print(sorted_numbers)

main()