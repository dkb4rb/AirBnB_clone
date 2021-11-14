#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
from os import name
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from shlex import split


dictionary_function = {"BaseModel": BaseModel}

def tokenize(text):
    tokened = split(text)
    return(tokened)


class HBNBCommand(cmd.Cmd):
    """
    Define cmd
    """
    prompt = "(hbnb)"

    def do_quit(self, args):
        """Exit this application"""
        return True

    def do_EOF(self, args):
        """Called when <Ctrl>-D is pressed"""
        return True

    def emptyline(self):
        """" shouldn’t execute anything """
        return cmd.Cmd.emptyline(self)

    def do_create(self, argv):
        """
            create new instance from BaseModel
            and print his id
        """
        cmdtk = tokenize(argv)
        """ Condition to evaluate if cmdtk or arguments is NULL"""
        if len(cmdtk[0]) == 0:
            print("** class name missing **")
        """ Condition to evaluate if argv[0] is equal to __class dict declare"""
        if cmdtk[0] in dictionary_function:
            first_instance = dictionary_function[cmdtk[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(first_instance.id)
        first_instance.name = "Juan"
        storage.save()

    def do_show(self, argv):
        """ Print an instance in str Representation"""

        command = tokenize(argv)
        if len(command) == 0:
            print("** class name missing **")
            return False
        if command[0] in dictionary_function:
            if len(command) > 1:
                key = command[0] + "." + command[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    
    def do_destroy(self, argv):
        """ Delete an instance based in the class""" 
        command = tokenize(argv)

        if len(command) == 0:
            print("** class name missing **")
        elif command[0] in dictionary_function:
            if len(command) > 1:
                key = command[0] + "." + command[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
    
    def do_all(self, argv):
        """ Printing all instances in to str Representation"""
        command = tokenize(argv)
        list_objects = []
        if len(command) == 0:
            for v in storage.all().values():
                list_objects.append(str(v))
            print("[", end="")
            print(", ".join(list_objects), end="")
            print("]")
        elif command[0] in dictionary_function:
            for k in storage.all():
                if command[0] in k:
                    list_objects.append(str(storage.all()[k]))
            print("[", end="")
            print(", ".join(list_objects), end="")
            print("]")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
