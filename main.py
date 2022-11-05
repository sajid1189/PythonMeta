"""
A small project to demonstrate the workflow of python's magic/dunder methods in combination with Meta class.
"""

from demo.classes import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Root(name="Sajid")
    try:
        name = root.name
        print(name)
    except AttributeError as e:
        print(e)

