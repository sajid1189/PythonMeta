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


class SpecialClass(metaclass=CustomMeta):

    def __init__(self, name: str):
        self.name = name


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