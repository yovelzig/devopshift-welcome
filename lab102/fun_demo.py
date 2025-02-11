from typing import *

# the same purpose to functio and function2 with lambda
# def something(a):
#     return a * 3
# something2 = lambda a: a * 3

def do_math(a: int, b: int, operation_fuction: callable) -> int:
    if len(operation_fuction.__annotations__) == 2:
        result = operation_fuction(a)
    else:
        result = operation_fuction(a, b)
    return result

def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b
op_map = { 
    'add': add,
    'multiply': multiply
}

# #
# הגדרת דקורטור (loggin_decorator)
# הדקורטור הוא פונקציה שמקבלת פונקציה (func) כפרמטר ומחזירה פונקציה עטופה (wrapped) חדשה.
# דקורטורים משמשים בדרך כלל כדי להוסיף התנהגות לפונקציה קיימת מבלי לשנות את הקוד המקורי שלה.
# פרמטרים עם טיפוסי רמז (func: Callable -> Callable)
# Callable: טיפוס שמייצג פונקציה (כל פונקציה שניתן לקרוא לה).
# -> Callable: מציין שהפונקציה loggin_decorator מחזירה פונקציה אחרת.
# הגדרת הפונקציה wrapper
# הפונקציה הפנימית wrapper מחליפה את הפונקציה המקורית ומוסיפה לה התנהגות נוספת.
# קלטים גמישים (*args, **kwargs)
# *args: אוסף של כל הארגומנטים הפוזיציוניים שנשלחו לפונקציה.
# **kwargs: אוסף של כל הארגומנטים המפורשים עם שמות (keyword arguments).
# הוספת התנהגות
# print(f'Function {func.__name__} called with args: {args} and kwargs: {kwargs}')
# מדפיס שם הפונקציה (func.__name__) ואת הארגומנטים שהתקבלו.
# קריאה לפונקציה המקורית
# return func(*args, **kwargs)
# מפעיל את הפונקציה המקורית עם אותם ארגומנטים שהתקבלו.
# החזרת ה-wrapper
# return wrapper
# מחזיר את הפונקציה החדשה שמוסיפה לוג של הקריאות
def loggin_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f'Function {func.__name__} called with args: {args} and kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper          
    
    
    

something_else : int = lambda x = int : x

a = something_else(1)
print(f"a is {a}")

def logging_wrapper(func: Callable):
    def new_func(*args, **kwargs):
        print(f"{func._name_} was called with arguments: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return new_func


@logging_wrapper #  add = logging_wrapper(add)   שקול לכתיבה הבאה:
def add(x: int, y: int) -> int: return x + y
# add_with_logging_wrapper = logging_wrapper(add);
@logging_wrapper
def sub(x: int, y: int) -> int: return x - y
# sub_with_logging_wrapper = logging_wrapper(sub);
@logging_wrapper
def mul(x: int, y: int) -> int: return x * y
@logging_wrapper
def div(x:int, y:int) -> int: return x / y
def mod(x: int, y: int) -> int: return x % y
@logging_wrapper
def int_as_str(x: int) -> str: return str(x)

@logging_wrapper # add logging_wrapper to power function 
def power(x:int, y: int) -> int: return x ** y


# explain the purpose of the function
# the function do_math is a function that gets 3 parameters 
# x, y, operation_functions
# the function checks the length of the annotations of the operation_functions
def do_math(x : int, y : int, operation_functions: Callable):
    print(f"{operation_functions._annotations_}")
    if(len(operation_functions._annotations_) == 2):
        result = operation_functions(x)
    else:
        result = operation_functions(x, y)
    return result

op = "plus"
x = 2
y = 2

op_map = {
    "plus": add,
    "minus": sub,
    "mul": mul,
    "div": div,
    "mod": mod,
    "power": power
}


result = do_math(x, y, op_map[op])
print(f"result is {result}")   