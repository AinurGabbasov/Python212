def args_decorator(fn):
    def wrap(*args):
        fn(*args)
        print(f"Среднеарифметическое чисел {args} = ", sum(args) / len(args))

    return wrap


@args_decorator
def print_full_name(*args):
    print(f"Сумма чисел {args} = ", sum(args))


print_full_name(2, 3, 3, 4)