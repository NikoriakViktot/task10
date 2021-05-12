

    # Task1

class Person:

    def __init__(self, name, surname, age, ):
        self.name = name
        self.surname = surname
        self.age = age


    def talk(self):
        print ('Hi, my name is ' + self.name + self.surname + self.age)

    Person.talk = talk



person = Person(
    "Jane",
    "Doe",
    "26 year"

)
print( person.talk)


# Task2




