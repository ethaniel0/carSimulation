file = open('b.txt', 'r')
lines = file.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', '')
duration, num_intersections, num_streets, num_cars, bonus_points = lines.pop(0).split(' ')
duration = int(duration)
num_intersections = int(num_intersections)
num_streets = int(num_streets)
num_cars = int(num_cars)

intersections = []
for i in range(num_intersections):
  intersections.append([]);

for i in range(num_streets):
  dat = lines[i+1].split()
  try:
    intersections[int(dat[0])].append(dat[2])
    intersections[int(dat[1])].append(dat[2])
  except:
    break

file = open('outb.txt', 'w')
print(num_intersections, file=file)
for i in range(num_intersections):
  print(i,file=file);
  print(len(intersections[i]),file=file)
  for k in intersections[i]:
    print(k,duration,file=file)