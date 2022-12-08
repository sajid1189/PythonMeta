import random
import time


class CustomMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"I am inside the CustomMeta.__call__ method.")
        print(f"I am going to run object.__new__ method. This will create a new object of type {cls}")
        obj = object.__new__(cls)
        print(f"We have created the object and allocated memory for it. Here is the object {obj}")

        print("We are going to attach an attribute called `creation_timestamp`.")
        setattr(obj, "creation_timestamp", time.time_ns())
        print(f"Here is the value of {obj.creation_timestamp}")
        print(f"Now we will initiate the object {obj}")
        obj.__init__(*args, **kwargs)
        print(f"We are done with metafying. Now we are handing you over the object. Wish you good luck with {obj}")
        return obj

    def __new__(cls, name, bases, dct):
        print(f"I am the __new__ of {cls} metaclass. I am called to create the"
              f" class that uses me as their metaclass. In this case I am creating the class {name}")
        print(f"My args = {name=}, {bases=}, {dct=}")
        print(f"I can do some magic. class {name} will have a new attribute called sticky and its value will be 100.")
        class_ = super().__new__(cls, name, bases, dct)
        class_.sticky = 100
        return class_


class SpecialClass(metaclass=CustomMeta):
    """
    __doc__ method uses this doc string
    """

    def __new__(cls, *args, **kwargs):
        print("---- you will not see me printed on the console because i do not get called. "
              "Since we have a metaclass, the metaclass's __new__ is called instead of me---------")
        # return super().__new__(cls, *args, **kwargs)

    def __init__(self, name: str):
        self.name = name


class DummyClass:

    def __new__(cls, *args, **kwargs):
        print(f"i am the overriden __new__  and i will not call my fellow"
              f" __init__. args = {args} and  kwargs = {kwargs}")
        # return super().__new__(cls, *args, **kwargs)

    def __init__(self, x):
        self.x = x
        # has no effect because __init__ is not being called by __new__


class NormalClass:

    def __init__(self, name: str, age: int = 20):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


def timestamped_object_factory(cls: type, *args, **kwargs) -> object:
    obj = object.__new__(cls, *args, **kwargs)
    setattr(obj, "creation_timestamp", time.time_ns())
    return obj


def better_timestamped_object_factory(cls: type, *args, **kwargs) -> object:
    obj = object.__new__(cls)
    obj.__init__(*args, **kwargs)
    if getattr(obj, "creation_timestamp", None):
        setattr(obj, "creation_timestamp", time.time_ns())
    return obj


class Foo:
    pass


# dynamically build a class
# by using type(<name>, <bases>, <dct>):
Bar = type('Bar', (Foo,), dict(attr=100))

"""
Bar = type('Bar', (Foo,), dict(attr=100))
is same as

class Bar(Foo):
    attr = 100

"""
