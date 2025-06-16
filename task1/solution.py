def strict(func):
    def wrapper(*args, **kwargs):
        check_type = list(func.__annotations__.values())[:-1]
        args_type = [type(arg) for arg in args]
        if check_type == args_type:
            return func(*args, **kwargs)
        else:
            raise TypeError
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError

