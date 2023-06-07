# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

class WizardPlayer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def attack(self):
        print("Attack!!!")

    def age_checker(self):
        if self.age >= 18:
            print("Acceptable")
        else:
            print("Not acceptable")

    @staticmethod
    def test_funx(n1, n2):
        return n1 + n2

    @classmethod
    def test_funx2(cls, n1, n2):
        return cls("Harry", 80)

class HeadWizard(WizardPlayer):
    def __init__(self, type, name, age):
        super().__init__(name, age)
        self.type = type

    def attack(self):
        return "Útok 2. stupňa"

    def avada_kedavra(self):
        return "Avada Kedavra"

"""#player1 = WizardPlayer("David", 23)
#print(player1.test_funx(20, 30))
#print(WizardPlayer.test_funx(60, 70))
#print(WizardPlayer.test_funx2(30, 20))"""

# player1 = WizardPlayer("David", 26)
# player2 = HeadWizard("good", "Snape", 35)
# print(player1.attack())
# print(player2.attack())
#
# # Introspection
# print(dir(player2))
# # Aneb player2.
# print("______________________")
#
# #Dunder methods začína s __
# print(player2.__dir__())
# print([5, 8, 4, 6].__len__())


# MRO Method Resolution Order
print(HeadWizard.mro())




######################

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# d_1 = Dog("Ando", 3)
# d_2 = Dog("Dando", 4)
# d_3 = Dog("Prando", 9)
#
# dogs = [d_1, d_2, d_3]
#
# def oldest(all_dogs):
#     oldest_dog_age = 0
#     for one_dog in all_dogs:
#         if one_dog.age > oldest_dog_age:
#             oldest_dog_age = one_dog.age
#     return oldest_dog_age
#
# print(oldest(dogs))





















