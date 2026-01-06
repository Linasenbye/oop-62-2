#Part 1
class User:
    def __init__(self, name, email, password):
        self.name = name
        self._email = email
        self.__password = password
 
    def show_email(self):
        return print(self._email)
    
    def check_password(self, password):
        if self.__password == password:
            return True
        return False
        
    def change_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            return print(self.__password)
        return None    

#Part 2
from abc import ABC, abstractclassmethod

class Transport(ABC):
    @abstractclassmethod

    def move(self):
        pass

class Car(Transport):
    def move(self):
        return print('Машина едет по дороге')
    

class Bicycle(Transport):
    def move(self):
        return print('Велосипед едет по велодорожке')
