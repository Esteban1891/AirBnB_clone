## 0x00 AirBnB Clone
![hbnb logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)
First project in the AirBnB clone series is about laying the framework for a simple [AirBnB](http://airbnb.com/) clone.\
We have created some base classes for recieving, serializing and deserializtion of information along with creating a console using Class cmd for added control of handling the information.

## Environment
Creation and testing-
* Ubuntu 14.04.5 LTS
* Vagrant VirtualBox
* Python 3
* PEP8 styling

## Repository Contents
### Directories and Classes
| Directory        | Class         | Description                                                                         |
|------------------|---------------|-------------------------------------------------------------------------------------|
| Model            | BaseModel     | Defines all common attributes/methods for other classes                             |
|                  | Amenity       | Defines amenities available                                                         |
|                  | City          | Defines state id and name of the city                                               |
|                  | Place         | Defines attributes like price by night, city id, number of rooms etc                |
|                  | Review        | Defines attributes like place id, user id and text description                      |
|                  | State         | Defines state name                                                                  |
|                  | User          | Defines user attributes like email, password, first and last names                  |
| model/engine     | FileStorage   | Class to create, save and reload instances                                          |
| console          | HBNBCommand   | Inherited from class cmd that will create, show, destroy, update and print instances|
| tests/test_models| Test_Amenity  | Testing methods in amenity                                                          |
|                  | TestBaseModel | Testing methods in BaseModel class                                                  |
|                  | TestCityModel | Testing class city attributes in BaseModel class                                    |
|                  | TestPlaceModel| Testing class city	attributes in BaseModel	class                                    |
|                  | TestReviewModel| Unittest cases for review class                                                    |
|                  | TestStateModel| Unittest for cases of state class                                                   |
|                  | TestUserModel | Unittest for cases of User class                                                    |
| tests/test_models/engine| TestFileStorage | Unittests to test File storage class                                       |

## Installation
This repository can be clones using the git provided url:\
``` $ git clone https://github.com/Esteban1891/AirBnB_clone.git ```\

## Console
The console is used to create, update, destroy and print instances of the classes.\

To start the console:\
``` ~/AirBnB_clone$ ./console ```

Example of use:
```
AirBnB_clone$ ./console.py
(hbnb) create BaseModel
c93ddfb5-f80c-4a70-bd9a-6c922e384a46
(hbnb) show BaseModel 7872aba3-eae1-4b93-a0c1-8932c96183e0
[BaseModel] (7872aba3-eae1-4b93-a0c1-8932c96183e0) {'id': '7872aba3-eae1-4b93-a0c1-8932c96183e0', 'created_at': datetime.datetime(2018, 2, 15, 1, 0, 42, 625486), 'updated_at': datetime.datetime(2018, 2, 15, 1, 0, 42, 625516)}
(hbnb) create
** class name missing **
(hbnb) show BaseModel
** instance id missing **

```
## Testing
The code can be tested using unittest in the tests directory by using the following command-
```AirBnB_clone$ python3 -m unittest discover tests```

## Bugs
This program is the embodiment of perfection. So no bugs.

## Credit
*Esteban De La Hoz* - [Github](https://github.com/Esteban18911) || [Twitter](https://twitter.com/Esteban18911)

*Eduardo Vega* - [Github](https://github.com/EduardoVega04) || [Twitter](https://twitter.com/eduardo_vega04)
