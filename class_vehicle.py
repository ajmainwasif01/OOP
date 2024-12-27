class Vehicle: 
    def __init__(self,max_speed, milage):
        self.speed = max_speed
        self.milage = milage

X = Vehicle(250, 100)

print("The model X has a maximum speed of", X.speed)
print("It will give a milage of" , X.milage)
