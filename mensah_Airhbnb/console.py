#!/usr/bin/python3
""" console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ class cmd """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """ EOF command"""
        print("")
        return True

    def do_quit(self, arg):
        """ quit command"""
        return True
    
    def do_create(self, arg):
        """ creates a user  """
        return True
    
    def emptyline(self) -> bool:
        return super().emptyline()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
