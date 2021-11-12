#!/usr/bin/python3

from models.base_model import BaseModel

def print_new_space_line():
    print("----------------> NEXT <------------------------")

def print_new_base_model():
    i = BaseModel()
    print("-----> ", type(i.created_at))
    print(f"{i.created_at}\n{i.updated_at}")
    print("{}".format(i.__dict__))
    print("\n\n")
    print("{}".format(i.__str__()))

def print_class_model():
    instance1 = BaseModel("Juan", "Duque")
    print(type(instance1.to_dict()))
    print(type(instance1.save()))
    print(type(instance1.id))
    print(type(instance1.created_at))
    print(type(instance1.updated_at))

if __name__ == "__main__":
    print_new_base_model()
    print_new_space_line()
    print_class_model()

