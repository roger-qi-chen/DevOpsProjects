from typing import List


class MyProfile:
    def __init__(self,
                 name: str,
                 age: int,
                 nicknames: List[str],
                 phone: str,
                 address: str):
        self.name = name
        self.age = age
        self.nicknames = nicknames
        self.phone = phone
        self.address = address

    def get_name(self):
        return self.name


class CarInsurance:
    def __init__(self,
                 profiles: List[MyProfile],
                 candidate: str,
                 rego: str,
                 brand: str,
                 year: int):
        self.profiles = profiles
        self.candidate = candidate
        self.rego = rego
        self.brand = brand
        self.year = year
        self.insurer = None

    def set_insurer(self):
        for profile in self.profiles:
            if self.candidate in profile.get_name():
                self.insurer = self.candidate

    def get_insurer(self):
        return self.insurer


def my_profile(name: str, age: int, nicknames: List[str]):
    print(f"My name is {name} and my age is {age}")
    print(f"I have many nicknames. e.g. {nicknames}")


if __name__ == '__main__':
    my_nicknames = ["goggle", "winston"]
    my_profile(name="Yu",
               age=18,
               nicknames=my_nicknames)

    yu_profile = MyProfile(name="Yu",
                           age=18,
                           nicknames=my_nicknames,
                           phone="62788",
                           address="400 George")
    davis_profile = MyProfile(name="Davis",
                              age=22,
                              nicknames=["genius"],
                              phone="37999",
                              address="400 George")
    my_profiles = [yu_profile, davis_profile]
    insurance = CarInsurance(profiles=my_profiles,
                             candidate="Yu",
                             rego="CZM59W",
                             brand="BMW",
                             year=1998)
    insurance.set_insurer()
    print(f"The insurer is {insurance.get_insurer()}")