#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
mod_json = my_model.to_dict()
print(mod_json)
print("JSON of my_model:")
for key in mod_json.keys():
    print("\t{}: ({}) - {}".format(key, type(mod_json[key]), mo_json[key]))

print("--")
my_new_model = BaseModel(**mod_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
