class Street:
  def __init__(self, startInt, endInt, streetName, timeTraveled):
    self.startInt = startInt
    self.endInt = endInt
    self.streetName = streetName
    self.timeTraveled = timeTraveled
    self.light = False

class Car:
  def __init__(self, secondsTraveled, streetPath):
    #streetpath should be an array
    self.secondsTraveled = secondsTraveled
    self.streetPath = streetPath
    self.streetNum = 0
    self.onStreet = streetPath[0]
    self.secondsThrough = 0
    self.atEnd = False
    self.arrived = False
    
  def update(self): # not completed, finish this
    # if the car isn't at the end of a street
    if not self.atEnd:
      self.secondsThrough += 1
      if (self.secondsThrough == self.onStreet.timeTraveled):
        self.atEnd = True
    # if the car is at the end of the street
    elif self.onStreet.light:
      # if the light is green, go forwards to the next street
      self.streetNum += 1
      if (self.streetNum == len(self.streetPath)): self.done = True
      else:
        self.onStreet = self.streetPath[self.streetNum]

    # how do we check the street
    

class Intersection:
  def __init__(self, num):
    self.waitingCars = []
    self.intNum = num
    self.actions = []


file = open('b.txt', 'r')
lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')
duration, num_intersections, num_streets, num_cars, bonus_points = lines.pop(0).split(' ')

streets = []
cars = []
intWithCars = []

lightLogs = []

# streets
for i in range(int(num_streets)):
  B, E, name, Time = lines.pop(0).split(' ')
  intBeg = Intersection(B)
  intEnd = Intersection(E)
  streets.append(Street(intBeg, intEnd, name, int(Time)))
  #lights.append(False)

# cars
for i in range(int(num_cars)):
  P = lines.pop(0).split(' ')

  my_streets = []
  for i in range(len(P) - 1):
    for street in streets:
      if P[i+1] == street.streetName:
        my_streets.append(street)
        break

  lenSeconds = 0
  for street in my_streets:
    lenSeconds += street.timeTraveled
    
  cars.append(lenSeconds, my_streets)

intersecitonPlan = []

for timeStep in range(duration):
  # update cars
  for car in cars:
    if not car.atEnd:
      car.update()
      if car.onStreet.timeTraveled == car.secondsThrough:
        car.onStreet.endInt.waitingCars.append(car)
        intWithCars.append(car.onStreet.endInt)
        car.atEnd = True
        car.secondsThrough = 0

  for intersection in intWithCars:
    if len(intersection.waitingCars) == 1:
      car = intersection.waitingCars[0]
      intersection.append(car.onStreet, timeStep)
      #timestep recorded so we can find out how long it turns green until the next light turns green. 
      intersecitonPlan.append(intersection)
    else:
      





'''
# intersection.before.append
# intersection.after.append
intersections = []
for i in range(int(num_intersections)): 
  intersections.append(Intersection(i))

for street in streets:
  # 
	intersections[street.startInt].after.append(intersections[street.endInt])
	intersections[street.endInt].after.append(intersections[street.startInt])


for second in range(duration):
'''
