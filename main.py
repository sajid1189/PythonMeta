"""
A small project to demonstrate the workflow of python's magic/dunder methods in combination with Meta class.
"""

from demo.classes import SpecialClass, NormalClass, timestamped_object_factory, better_timestamped_object_factory, DummyClass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timestamped_obj = SpecialClass(name="Max")
    print(f"The timestamped_obj object was created at {getattr(timestamped_obj, 'creation_timestamp', None)}")

    normal_obj = NormalClass(name="Michael")
    print(f"The normal_obj object was created at {getattr(normal_obj, 'creation_timestamp', 'Unknown time')}")

    factory_manufactured_normal_obj = timestamped_object_factory(NormalClass)
    print(f"The normal_obj object was created at:"
          f"# {getattr(factory_manufactured_normal_obj, 'creation_timestamp', 'Unknown time')}")

    # Since the __init__  of factory_manufactured_normal_obj was not called we can't access the name attribute.
    try:
        factory_manufactured_normal_obj.get_name()
    except AttributeError:
        print(f" We are handling AttributeError exception because"
              f" factory_manufactured_normal_obj's get_name() could not access the name attribute.")

    another_factory_manufactured_normal_obj = better_timestamped_object_factory(NormalClass, "Empowered", age=55)
    print(f" We successfully accessed the get_name of NormalClass object. Here is it's name:"
          f" {another_factory_manufactured_normal_obj.get_name()}")
    print(f"Like __call__ of CustomMeta said, SpecialClass will have an attribute and its value is 100. This is {SpecialClass.sticky == 100}")
    d = DummyClass(x=1)
    # d does not have attr x since itS __new__ did not call __init__
    assert hasattr(d, "x") is False
