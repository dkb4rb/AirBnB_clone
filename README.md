# **0x00. AirBnB clone - The console** 🖨
## Project clone [AirBnB] ⬅️
![N|Solid](https://raw.githubusercontent.com/KevinAndresG/AirBnB_clone/main/assets/Holberton.png)

### *Command interpreter to manage your AirBnB objects*
This is the first step in creating the complete web application: the AirBnB clone. This first step is very important because you will use what is built during this project with all the other projects below: HTML / CSS templates, database storage, API, front-end integration ...

With this command interpreter you can manipulate data for the AirBnB page without the need for a visual interface, since through the console you can create, store, update, delete data, saving the information in a JSON file.

## _Examples of_ AirBnB_clone usage 🖥️
Once the repository is cloned in the main folder, you will have to write the code to start.
**Code to start:** ```./console.py```

**Class name available:** ▶️

- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

**Interpreter commands:** ▶️
It is used to give functionality to the console from the command line, in this case we have:

| Command  |Description | Example
| ------ | ------ | ------ |
|EOF| Exit command interpreter | $ <Ctrl>-D is pressed
| quit | Exit command interpreter | $ quit
| help | Displays the help available for the created commands | $ help "command"
| create | Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.| $ create "class name"
| show | Prints the string representation of an instance based on the class name and id. | $ show "class name" "id"
| destroy | Deletes an instance based on the class name and id | $ destroy "class name" id"
| update | Updates an instance based on the class name and id by adding or updating attribute. | $ update "class name" or "id"
| all | Prints all string representation of all instances based or not on the class name. | $ all "class name" or all

**Execute:** ▶️

- Example when you run the help command, it displays help for each command created.
``` $ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
- Example when the class does not exist, if information is missing to execute the command and if the instance does not exist
```
$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
```
- Example when we create data, it is displayed and destroyed.
```
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```


## _Installation_ ⚙️
To use this custom _printf function follow the steps below:
 - Clone the repository
 ```$ git clone https://github.com/KevinAndresG/AirBnB_clone/tree/main```
- Enter the AirBnB_clone folder
```$ cd AirBnB_clone```
- To access the console and the commands run:
```$ ./console.py ```


## License

**Free Software**

[![N|Solid](https://i.postimg.cc/FKh7hgp9/pngegg.png)](https://twitter.com/Juan_Duque0)
Juan Duque
[![N|Solid](https://i.postimg.cc/FKh7hgp9/pngegg.png)](https://twitter.com/KevinAndresG22)
Kevin García
[![N|Solid](https://i.postimg.cc/FKh7hgp9/pngegg.png)](https://twitter.com/Lisethav55)
Liseth Arias

[//]: # (These are reference links used in the body of this note. - )

   [AirBnB]: <https://www.airbnb.com.co/>
