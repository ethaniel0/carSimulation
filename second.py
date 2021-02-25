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
    self.onStreet = streetPath[0]
    self.secondsThrough = 0

class Intersection:
	def __init__(self, num):
		self.before = []
		self.after = []
		self.num = num


file = open('b.txt', 'r')
lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')
duration, num_intersections, num_streets, num_cars, bonus_points = lines.pop(0).split(' ')

streets = []
lights = []
cars = []

## streets
for i in range(int(num_streets)):
	B, E, name, Time = lines.pop(0).split(' ')
	streets.append(Street(int(B), int(E), name, int(Time)))
  lights.append(False)

for i in range(int(num_cars)):
  P = lines.pop(0).split(' ')

  my_streets = []
  for i in range(len(P) - 1):
    my_streets.append(P[i+1]) # adds street name
  cars.append(Car(P[0], my_streets))

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
