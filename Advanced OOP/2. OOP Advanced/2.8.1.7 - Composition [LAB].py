'''
Objectives

    improving the student's skills in operating with inheritance and composition

Scenario

Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.

Your task is to :

    define classes representing:
        tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
        engine; methods available: start(), stop(), get_state(); attribute available: fuel type
        vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN
    based on the classes defined above, create the following objects:
        two sets of tires: city tires (size: 15), off-road tires (size: 18)
        two engines: electric engine, petrol engine
    instantiate two objects representing cars:
        the first one is a city car, built of an electric engine and city tires
        the second one is an all-terrain car build of a petrol engine and off-road tires
    play with the cars by calling methods responsible for interaction with components.

'''

# ===== BASE CLASSES =====
class Tires():
    def __init__(self, size: int) -> None:
        self.size = size
    
    def get_pressure(self) -> None:
        print("Checking air pressure...")
    
    def pump(self) -> None:
        print("Pumping up tires...")

class Engine():
    def __init__(self, fuel_type: str) -> None:
        self.fuel_type = fuel_type
        self.___state = False
    
    def start(self) -> None:
        self.___state = True
        print("Starting engine...")
    
    def stop(self) -> None:
        self.___state = False
        print("Stopping engine...")
    
    def get_state(self) -> None:
        if self.___state:
            print("Engine is running.")
        else:
            print("Engine is off.")
    
class Vehicle:
    def __init__(self, VIN: int, engine: Engine, tires: Tires) -> None:
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

# === Tires Subclasses ===
class CityTires(Tires):
    def __init__(self) -> None:
        super().__init__(15)

class OffRoadTires(Tires):
    def __init__(self) -> None:
        super().__init__(18)

# === Engine Subclasses ===
class ElectricEngine(Engine):
    def __init__(self) -> None:
        super().__init__("Electricity")

class PetrolEngine(Engine):
    def __init__(self) -> None:
        super().__init__("Unleaded")


# ===== TESTING =====

# City Car
city_car = Vehicle(12345, ElectricEngine(), CityTires())
city_car.engine.start()
city_car.engine.get_state()
city_car.engine.stop()
city_car.engine.get_state()
print(city_car.engine.fuel_type)

city_car.tires.get_pressure()
city_car.tires.pump()
print(city_car.tires.size)

# All Terrain Car
all_terrain_car = Vehicle(54321, PetrolEngine(), OffRoadTires())
all_terrain_car.engine.start()
all_terrain_car.engine.get_state()
all_terrain_car.engine.stop()
all_terrain_car.engine.get_state()
print(all_terrain_car.engine.fuel_type)

all_terrain_car.tires.get_pressure()
all_terrain_car.tires.pump()
print(all_terrain_car.tires.size)