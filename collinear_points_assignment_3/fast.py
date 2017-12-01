#! /bin/bash/python3

import math
import operator

class PointAngle:
	def __init__(self, xy):
		self.point = xy
		self.angle = 0

	def SetAngle(self, xy):
		y = xy.point[1] - self.point[1]
		x = xy.point[0] - self.point[0]
		if x == 0:
			self.angle = 90.0
		elif y == 0:
			self.angle = 0.0
		else:
			self.angle = math.degrees(math.atan(y/x))

def testCollinearPoints(points):
	pointAngle = []
	completedPoints = []

	# Construct structure continaing a point and initial angle set to 0
	for elem in points:
		pointAngle.append(PointAngle(elem))


	for elem in pointAngle:
		if elem.point in completedPoints:
			continue
		
		# Create a copy of structure
		listCopy = list(pointAngle)
		# For each point, calc angle between itself and a reference point
		for elem2 in listCopy:
			elem2.SetAngle(elem)
		
		# Sort the structure based on the angle between points
		listCopy.sort(key=operator.attrgetter('angle'))
		length = len(listCopy)

		# Check if there are atleast 3 points at same angle with respect to reference point
		# If so, then add them to completed list to avoid duplicates
		prev = listCopy[0].angle
		count = 1
		for i in range(1, length):
			if listCopy[i].angle == prev:
				count += 1
			else:
				if count > 2:
					print("Points", end=" ")
					j = 0
					while count > 0:
						print(listCopy[i-1-j].point, end=" ")
						completedPoints.append(listCopy[i-1-j].point)
						j += 1
						count -= 1
					print(elem.point, end = " ")
					completedPoints.append(elem.point)
					print("are collinear")
				count = 1
				prev = listCopy[i].angle

def main():
	list1 = [(10000,0), (0,10000), (3000,7000), (7000,3000), (20000,21000), (3000,4000), (14000,15000), (6000,7000)]
	list2 = [(19000,10000), (18000,10000), (32000,10000), (21000,10000), (1234, 5678), (14000,10000)]
	list3 = [(10000,0), (0,10000), (3000,7000), (7000,3000)]
	testCollinearPoints(list3)

if __name__ == "__main__": main()
