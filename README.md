![link](https://i.imgur.com/X8EA2Zv.png)

## Description
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

Each task is linked and will help you to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

### Command interpreter funcionalities:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Execution
The console executes in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```
But also in non-interactive mode: (like the Shell project in C)

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create

        Create command to create a new instance according Class name.
        Print the assigned id.
        Usage: create <class name>
        Classes: [BaseModel, User, Place, State, City, Amenity, Review]
        
(hbnb) 
(hbnb) quit
$
```
## Supported commands
|Command| Description |
|--|--|
| **create** | Creates a new instance based on the [class name], saves it (to a JSON file) and prints the [ID]. `$ create BaseModel` |
| **show** | Prints the string representation of an instance based on the [class name] and [ID]. `$ show BaseModel 1234-1234-1234` |
| **destroy** | Deletes an instance based on the [class name] and [ID] (saves changes into a JSON file). `$ destroy BaseModel 1234-1234-1234` |
| **all** | Prints all string representation of all instances based or not on the [class name]. `$ all BaseModel` or `$ all` | 
| **update** | Updates an instance based on the [class name] and [ID] by adding or updating attribute (saves changes into a JSON file). `$ update BaseModel 1234-1234-1234 email "airbnb@holbertonschool.com"`|
| **EOF** | Quits the program by EOF (CTRL+D) |
| **quit** | Exits the console |


## Alternative usage
|Command| Example |
|--|--|
|[class name].all()| BaseModel.all() |
|[class name].count()| BaseModel.count() |
|[class name].show()| BaseModel.show() |
|[class name].destroy()| BaseModel.destroy() |

## Project Learning Objetives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

### Resources
* [Python cmd Module](https://docs.python.org/3.4/library/cmd.html)
* [cmd - Create line-oriented command processors](https://pymotw.com/2/cmd/)
* [Unit testing framework](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [A simple Python unittest](https://www.pythonsheets.com/notes/python-tests.html)
* [How To Use *args and **kwargs in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)

# Authors :)

***Carlos Berrio*** @CarlosBerro6
 <a href="https://twitter.com/CarlosBerro6" rel= "nofollow"> <img width="18px" align="center"
src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg" style="max-width: 100%;"> <a href="https://github.com/carlosberrio"> <img width="18px" align="center" src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg" style="max-width: 100%;"></a>

***Santiago Zapata*** @Santiag72319908 <a href="https://twitter.com/Santiag72319908" rel= "nofollow"> <img width="18px" align="center"
src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/twitter.svg" style="max-width: 100%;"> <a href="https://github.com/Santiago23z"> <img width="18px" align="center" src="https://raw.githubusercontent.com/rahulbanerjee26/githubAboutMeGenerator/main/icons/github.svg" style="max-width: 100%;"></a>
