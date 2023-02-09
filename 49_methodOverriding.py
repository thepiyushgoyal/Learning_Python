import os
os.system('cls')
 
class car:
    def __init__(self,model):
        self.model = model
    def showCar(self):
        return self.model

class tyota(car):
    def __init__(self, carModel):
        self.carModel = carModel
        super().__init__(carModel)
    def showCar(self):
        print("Model: ",super().showCar())

class hundayi(car):
    def __init__(self, carModel):
        self.carModel = carModel
        super().__init__(carModel)
    def showCar(self):
        print("Model: ",super().showCar())

class suzuki(car):
    def __init__(self, carModel):
        self.carModel = carModel
        super().__init__(carModel)
    def showCar(self):
        print("Model: ",super().showCar())

c1 = tyota('innova')
c2 = tyota('fortuner')
c3 = hundayi('verna')
c4 = hundayi('creta')
c5 = suzuki('alto')
c6 = suzuki('breeza')

c1.showCar()
c2.showCar()
c3.showCar()
c4.showCar()
c5.showCar()
c6.showCar()
