import os
os.system('cls')
 
class Country:
    def __init__(self,country):
        self.country = country
    def show(self):
        print(f"Country: {self.country}")
class State(Country):
    def __init__(self,state,country):
        super().__init__(country)
        self.state = state
    def show(self):
        super().show()
        print(f"State: {self.state}")
class City(State):
    def __init__(self,city,state,country):
        super().__init__(state,country)
        self.city = city
    def show(self):
        super().show()
        print(f"City: {self.city}")

c = City('Muktsar','Punjab','India')
c.show()