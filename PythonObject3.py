import math

class Point:

    def __init__(self, x=0, y=0):
        self.move(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 +       #Pathagorean Theorem!
            (self.y - other_point.y)**2
        )

point1 = Point()
point2 = Point()

point1.reset()
point2.move(5,0)

print(point2.calculate_distance(point1))

point1.move(3,4)
print(point2.calculate_distance(point1))
