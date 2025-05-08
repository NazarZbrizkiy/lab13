import types
import inspect

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

code = """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
"""
namespace = {}
exec(code, namespace)
Person = namespace['Person']

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def log_instance_creation(cls):
    orig_init = cls.__init__
    def __init__(self, *args, **kwargs):
        print(f"Створено екземпляр класу: {cls.__name__}")
        orig_init(self, *args, **kwargs)
    cls.__init__ = __init__
    return cls

@log_instance_creation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @log_call
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("Ivan", 30)
p.greet()