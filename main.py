class vehicle:
    def __init__(self,VIN,engine,tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires
        
class tires:
    def __init__(self,size):
        self.size = size
        
    def get_pressure(self):
        print(f"Returning pressure of the tires size: {self.size}")
        
    def pump(self):
        print("Pumping tires...")


class engine:
    def __init__(self,fuelType):
        self.fuelType = fuelType
        self.sw = False
    def start(self):
        if self.sw:
            print("Engine has already started.")
        else:
            self.sw = True
            print("Engine started.")
    def stop(self):
        if self.sw:
            self.sw=False
            print("Engine stopped.")
        else:
            print("Engine has already stopped")
        
    def get_state(self):
        if self.sw:
            print("Engine currently on")
        else:
            print("Engine currently on")


cityTires = tires(15)
offroadTires = tires(18)
electricEng = engine("Electric engine")
petrolEng = engine("Petrol engine")

cityCar = vehicle("1HGCM82633A123456",electricEng,cityTires)

print(cityCar.VIN)
cityCar.engine.start()
cityCar.engine.get_state()
cityCar.engine.stop()
cityCar.tires.get_pressure()
cityCar.tires.pump()



allterrainCar = vehicle("JTMZD33V375060789",petrolEng,offroadTires)

print(allterrainCar.VIN)
allterrainCar.engine.start()
allterrainCar.engine.get_state()
allterrainCar.engine.stop()
allterrainCar.tires.get_pressure()
allterrainCar.tires.pump()
