from .Temperature import Temperature
from .Space import Space

class Interpolation():
    # Argument !
    delta_parameters = None
    c_parameters = None
    lamda = 1  
    sensors = []
    storage = None
    temperatures = None
    # Result !
    number_of_blocks = 0
    mark_interpolation = None # Check sensor have been multiple when we loop 3 dimension
    first_interpolation = None

    # Create first interpolation
    def __init__(self, sensors, storage):
        self.sensors = sensors 
        self.storage = storage
        self.first_interpolation = [[ ['#' for col in range(self.storage.z_max +1)] for col in range(self.storage.y_max+1)] for row in range(self.storage.x_max+1)]
        self.mark_interpolation = [[ [True for col in range(self.storage.z_max +1)] for col in range(self.storage.y_max+1)] for row in range(self.storage.x_max+1)]
        self.number_of_blocks = (self.storage.x_max +1)*(self.storage.y_max +1)*(self.storage.z_max +1)
        # Fill existed temperature
        for sensor in self.sensors:
            self.first_interpolation[sensor.x][sensor.y][sensor.z] = sensor.temperature
        self.temperatures = Temperature()
        self.temperatures.generate_temperatures(self.first_interpolation, self.storage)

    # Call after first_interpolation have called
    def set_temperatures(self, space_of_storage): 
        x_min = space_of_storage["x_min"]
        x_max = space_of_storage["x_max"]
        y_min = space_of_storage["y_min"]
        y_max = space_of_storage["y_max"]
        z_min = space_of_storage["z_min"]
        z_max = space_of_storage["z_max"]
        space = Space(x_min, y_min, z_min, x_max, y_max, z_max)
        self.temperatures = Temperature()
        self.temperatures.generate_temperatures(self.first_interpolation, space)
        print(self.temperatures)

    # Find c_parameters
    def generate_c(self):
        self.c_parameters = {
            "c0": self.temperatures.p000, 
            "c1": self.temperatures.p100 - self.temperatures.p000,
            "c2": self.temperatures.p010 - self.temperatures.p000,
            "c3": self.temperatures.p001 - self.temperatures.p000,
            "c4": self.temperatures.p110 - self.temperatures.p010 - self.temperatures.p100 + self.temperatures.p000,
            "c5": self.temperatures.p011 - self.temperatures.p001 - self.temperatures.p010 + self.temperatures.p000,
            "c6": self.temperatures.p101 - self.temperatures.p001 - self.temperatures.p100 + self.temperatures.p000,
            "c7": self.temperatures.p111 - self.temperatures.p011 - self.temperatures.p101 - self.temperatures.p110 + self.temperatures.p100 + self.temperatures.p001 + self.temperatures.p010 - self.temperatures.p000
        }

    # Find delta parameters
    def generate_delta(self, point, space):
        self.delta_parameters = {
            "delta_x": (point.get("x") - space.get("x_min")) / (space.get("x_max") - space.get("x_min")),
            "delta_y": (point.get("y") - space.get("y_min")) / (space.get("y_max") - space.get("y_min")),
            "delta_z": (point.get("z") - space.get("z_min")) / (space.get("z_max") - space.get("z_min"))
        }

    # Set value of lamda
    def set_lamda(self, unit):
        self.lamda = unit
    
    # Prepare for unknown point of secondary sensor - Call it after init this obj and called for c_parameters
    def prepare_unknown_sensors(self, space):
        count = 0
        print(space)
        x_lst = [ space.get("x_min"), space.get("x_max") ]
        y_lst = [ space.get("y_min"), space.get("y_max") ]
        z_lst = [ space.get("z_min"), space.get("z_max") ]
        for x in x_lst:
            for y in y_lst:
                for z in z_lst:
                    point = {
                        "x": x,
                        "y": y,
                        "z": z
                    }
                    print(point)
                    if self.first_interpolation[x][y][z] != "#":
                        continue
                    count += 1
                    self.generate_delta(point, {
                        "x_min":self.storage.x_min,
                        "y_min":self.storage.y_min,
                        "z_min":self.storage.z_min,
                        "x_max":self.storage.x_max,
                        "y_max":self.storage.y_max,
                        "z_max":self.storage.z_max
                    })
                    self.first_interpolation[x][y][z] = self.generate_temperature(point)
                    print("["+str(x)+"]["+str(y)+"]["+str(z)+"] = "+str(self.first_interpolation[x][y][z]))
        return count

    # Find only a point's temperature
    def generate_temperature(self, point):
        value_of_point = self.c_parameters.get("c0") + (self.c_parameters.get("c1")*self.delta_parameters.get("delta_x")) + (self.c_parameters.get("c2")*self.delta_parameters.get("delta_y")) + (self.c_parameters.get("c3")*self.delta_parameters.get("delta_z")) + (self.c_parameters.get("c4")*self.delta_parameters.get("delta_x")*self.delta_parameters.get("delta_y")) + (self.c_parameters.get("c5")*self.delta_parameters.get("delta_y")*self.delta_parameters.get("delta_z")) + (self.c_parameters.get("c6")*self.delta_parameters.get("delta_z")*self.delta_parameters.get("delta_x")) + (self.c_parameters.get("c7")*self.delta_parameters.get("delta_x")*self.delta_parameters.get("delta_y")*self.delta_parameters.get("delta_z"))
        return value_of_point
    
