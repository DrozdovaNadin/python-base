# Написать декоратор для логирования(вывод в консоль) типов
# позиционных аргументов функции:

def type_logger(func):
    def type_wrapper(*args, **kwargs):
        # print(*args,**kwargs)
        markup = func(*args, **kwargs)
        for i in args:
            c = type(i)
            # print(c)
            s = ', '.join(f'"{k}" = {v} : {type(v)}' for k, v in kwargs.items())
            # for k, v in kwargs.items():
            #     # print(k, v)
            #     s = ', '.join(f'"{k}" = {v} : {type(v)}' for k, v in kwargs.items())

        string_name = func.__name__
        print("Call for:",string_name)
        print(i,':',c)
        print(s)
        print('Rezult:', markup, 'type:', c)

    return type_wrapper


@type_logger
def render_input(*args,**kwargs):
   return 1

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
# render_input(1, a = 2, b = True, c = "q")





