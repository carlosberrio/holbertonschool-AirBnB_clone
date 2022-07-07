#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
import shlex
import cmd
import re
import json
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter implementation"""
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'City',
               'State', 'Place', 'Amenity', 'Review']

    def do_create(self, arg):
        """create command to create a new instance according with
        the Class name.
        Print the assigned id.
        Usage: create <class name>
        Classes: [BaseModel, User, Place, State, City, Amenity, Review]"""
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_update(self, arg):
        """update command to update an isntance based on the class name
        and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        inputs = shlex.split(arg)
        if arg == "" or arg is None or len(arg) == 0:
            print("** class name missing **")
        elif inputs[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(inputs) == 1:
            print("** instance id missing **")
        else:
            class_name = inputs[0]
            obj_id = inputs[1]
            obj_key = "{}.{}".format(class_name, obj_id)
            if obj_key not in storage.all():
                print("** no instance found **")
            elif len(inputs) < 3:
                print("** attribute name missing **")
            elif len(inputs) < 4:
                print("** value missing **")
            else:
                attribute = inputs[2]
                value = self.analyze(inputs[3])
                setattr(storage.all()[obj_key], attribute, value)
                storage.all()[obj_key].save()

    def analyze(self, line):
        """verifies if line is float or int value and if so,
        change the type of line"""
        if line.isdigit():
            return int(line)
        if line.replace(".", "", 1).isdigit():
            return float(line)
        return line

    def do_show(self, arg):
        """show command to print the string representation of an isntance
        based on the class name and id.
        Usage: show <class name> <id>"""
        inputs = arg.split(" ")
        if arg == "" or arg is None:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(inputs[0], inputs[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[obj_key])

    def do_destroy(self, arg):
        """Destroy command to delete an isntance based
        on the class name and id.
        Usage: destroy <class name> <id>"""
        inputs = arg.split(" ")
        if arg == "" or arg is None:
            print("** class name missing **")
        elif inputs[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(inputs[0], inputs[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[obj_key]
                storage.save()

    def do_all(self, arg):
        """All commands to print all string representation af alla instances
        based or not on the class name.
        Usage: all <class name (optional)>
        E.g: all       -------Prints all instances
             all user  -------Prints user instances"""
        inputs = arg.split(" ")
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        else:
            if inputs[0] in HBNBCommand.classes:
                print([str(obj) for obj in objs.values()
                       if type(obj).__name__ == arg])
            else:
                print("** class doesn't exist **")

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to quit and exit the program by EOF (CTR+D)"""
        return True

    def emptyline(self):
        """this command replaces default emptyline(), with an empty line
        + enter shouldn't execute anything
        """
        return False

    def count(self, arg):
        """Count command to retrieve the number of instances of a class
        usage: <class name>.count()"""
        if arg in HBNBCommand.classes:
            c = 0
            for obj in storage.all().values():
                c += 1 if obj.__class__.__name__ == arg else 0
                print(c)
        else:
            print("** class doesn't exits **")

    def default(self, arg):
        """Executes line when it does not match any class command
        Arg <string>: <class name>.command("optional parameters")
        E.g. User.count() ----- <cls>.count() Must be used without parameters
             User.all() ------ <cls>.all() Mut be used witout parameters
             User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
             User.update("38f22813-2753-4d42-b37c-67a17f1e4f88",
                                        {'first_name': "Jhon", "age": 89}"""

        met_rgx = re.search(r"^(\w+)\.(\w+)\(\)$", arg)
        arg_rgx = re.search(r"^(\w+)\.(\w+)\(([^)]+)\)$", arg)
        dic_rgx = re.search(r"^(\w+)\.(\w+)\(([^)]+)\, \s+(\{[^)]+\})\)$", arg)

        if met_rgx:
            class_name = met_rgx.group(1)
            command = met_rgx.group(2)
            if command == 'all':
                self.do_all(class_name)
            elif command == 'count':
                self.count(class_name)

        elif dic_rgx:
            command = dic_rgx.group(2)
            class_name = dic_rgx.group(1)
            obj_id = dic_rgx.group(3).replace('"', '')

            if class_name not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            if "{}{}".format(class_name, obj_id) not in storage.all():
                print("** no instance found **")
                return

            try:
                obj_dic = json.loads(dic_rgx.group(4).replace("'", '"'))
            except Exception:
                print("** value missing **")
                return

            if command == 'update':
                for key, value in obj_dic.items():
                    line = '{} {} {} {} "{}"'.format(
                        command, class_name, obj_id, key, str(value))
                    self.onecmd(line)
            else:
                print("** Check input **")

        elif arg_rgx:
            command = arg_rgx.group(2)
            class_name = arg_rgx.group(1)
            arguments = arg_rgx.group(3).replace(',', '')
            args_ls = shlex.split(arguments)

            if command == 'update':
                try:
                    attribute = args_ls[1]
                    value = args_ls[2]
                except Exception:
                    print("** Attribute or value missing **")
                    return
                line = '{} {} {} "{}"'.format(
                    command, class_name, args_ls[0], attribute, str(value))

            else:
                line = '{} {} {} {}' "{}".format(
                    command, class_name, args_ls[0])

            self.onecmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
