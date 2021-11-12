#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from shlex import split

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
        raise SystemExit

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
        tokenedcmd = tokenize(argv)
        first_name = BaseModel()
        first_name.name = argv
        storage.save()
        print(first_name.id)
        print(argv)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
