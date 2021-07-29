# Python-Essentials-LAB-3.4.1.14-Points-on-a-plane

**Objectives**

•	improving the student's skills in defining classes from scratch;

•	defining and using instance variables;

•	defining and using methods.

**Scenario**

Let's visit a very special place - a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Each point located on the plane can be described as a pair of coordinates customarily called x and y. We expect that you are able to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.

The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

This is how we imagine the class:

•	it's called Point;

•	its constructor accepts two arguments (x and y respectively), both default to zero;

•	all the properties should be private;

•	the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);

•	the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;

•	the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;

**Given test case**
```
point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
```

**Expected output**
```
1.4142135623730951
1.4142135623730951
```

**Complete code includes**
```
class Point:
    def __init__(self, x=0.0, y=0.0):
        # This constructor obviously creates  __x and __y properties
        # The only feature is the privateness of these proprties

    def getx(self):
        # Simply returns value of __x

    def gety(self):
        # Simply returns value of __y

    def distance_from_xy(self, x, y):
        # Uses math.hypot() to calculate distance to the point specified as two coords 
    def distance_from_point(self, point):
        # Uses self.distance_from_xy()
        # to calculate distance to the point given as another Point class
```
