#!/usr/bin/python3

from models.base_model import BaseModel

if __name__ == "__main__":

    i = BaseModel()
    print("-----> ", type(i.created_at))
    print(f"{i.created_at}\n{i.updated_at}")
    print("{}".format(i.__dict__))

    print("\n\n")

    print("{}".format(i.__str__()))
