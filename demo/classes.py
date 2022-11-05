import random


class CustomMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"I am a blocker of {cls.__name__}. I won't let you proceed fro here")
        obj = object.__new__(cls)
        obj.__init__(*args, **kwargs)
        return obj


class Root(metaclass=CustomMeta):

    def __init__(self, name:str):
        self.name = name

    def greet(self):
        print("Hi!")


class Sub1(Root):

    def greet(self):
        print("You are in Sub1")

    def dummy(self):
        print("dummy of Sub1")


class Sub2:

    def foo(self):
        print("You are in Sub1")

    def bar(self):
        print("dummy of Sub1")


class Child(Sub1, Sub2):
    def __init__(self, name: str):
        self.name = name


def factory(cls: type, *args) -> object:
    return object.__new__(cls, *args)
