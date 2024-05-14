from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n\t\t{args}")
        print(f"\n\t\t{kwargs}")
        print("\tAntes de llamar a la función")
        result = func(*args, **kwargs)
        print("\tDespués de llamar a la función")
        return result.upper()
    return wrapper

@my_decorator
def greet(name):
    """Función para saludar a alguien"""
    return(f"Hola, {name}!")
    
print(greet("Juan"))

print(greet.__name__)

print(greet.__doc__)