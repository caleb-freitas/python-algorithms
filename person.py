from datetime import datetime

class Person:

    # class variable
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    # class methods
    def __init__(self, name, age, eating=False, speaking=False):
        # instance variables
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def speak(self, subject):
        if self.eating:
            print(f'{self.name} can\'t talk by eating.')
            return

        if self.speaking:
            print(f'{self.name} is alreay speaking.')
            return
        
        print(f'{self.name} is speaking about {subject}.')
        self.speaking = True

    def stop_speak(self):
        if not self.speaking:
            print(f'{self.name} is not talking.')
            return
        
        print(f'{self.name} stop talk.')
        self.speaking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating.')
            return
        
        if self.speaking:
            print(f'{self.name} can\'t eat talking')
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
            return
        
        print(f'{self.name} stop eating.')
        self.eating = False

    def get_year(self):
        return self.current_year - self.age

# class instance
person = Person('Caleb', 21)