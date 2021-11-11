#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
