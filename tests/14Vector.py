# Vertex Classes unit test

# importing libraries
import sys
sys.path.append("C:/Users/wassimj/Documents/GitHub")

import topologicpy
import topologic
from topologicpy.Vertex import Vertex
from topologicpy.Edge import Edge
from topologicpy.Cluster import Cluster
from topologicpy.Wire import Wire
from topologicpy.Face import Face
from topologicpy.Shell import Shell
from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Topology import Topology
from topologicpy.Vector import Vector
import math
# Object for test case
f = Face.Rectangle()


# Case 1 - Angle
# test 1
angle = Vector.Angle([1,0,0], [0,1,0])
assert angle == 90, "Vector.Angle. Should be 90"

# Case 2 - AzimuthAltitude
# test 1
dictionary = Vector.AzimuthAltitude([1,0,0], mantissa=4)
assert dictionary['azimuth'] == 90, "Vector.AzimuthAltitude. Azimuth Should be 90.0"
assert dictionary['altitude'] == 0, "Vector.AzimuthAltitude. Altitude Should be 0.0"

# Case 3 - ByAzimuthAltitude
# test 1
vector = Vector.ByAzimuthAltitude(azimuth=0, altitude=0, north=0, reverse=False)
assert vector == [0.0,1.0,0.0], "Vector.ByAzimuthAltitude. Should be [0,1,0]"

# Case 4 - ByCoordinates
# test 1
vector = Vector.ByCoordinates(2,3,4)
assert vector == [2,3,4], "Vector.ByCoordinates. Should be [2,3,4]"

# Case 5 - ByVertices
v1 = Vertex.ByCoordinates(10,0,0)
v2 = Vertex.ByCoordinates(20,0,0)
# test 1
vector = Vector.ByVertices([v1,v2], normalize=True)
assert vector == [1,0,0], "Vector.ByAzimuthAltitude. Should be [1,0,0]"
# test 2
vector = Vector.ByVertices([v1,v2], normalize=False)
assert vector == [10,0,0], "Vector.ByAzimuthAltitude. Should be [10,0,0]"

# Case 6 - CompassAngle
# test 1
vectorA = [0,1,0]
vectorB = [0,1,0]
angle = Vector.CompassAngle(vectorA, vectorB)
assert angle == 0, "Vector.CompassAngle. Should be 0"

# test 2
vectorA = [0,1,0]
vectorB = [1,1,0]
angle = Vector.CompassAngle(vectorA, vectorB)
assert angle == 45, "Vector.CompassAngle. Should be 45"

# test 3
vectorA = [0,1,0]
vectorB = [1,0,0]
angle = Vector.CompassAngle(vectorA, vectorB)
assert angle == 90, "Vector.CompassAngle. Should be 90"

# test 4
vectorA = [0,1,0]
vectorB = [1,-1,0]
angle = Vector.CompassAngle(vectorA, vectorB)
assert angle == 135, "Vector.CompassAngle. Should be 135"

# test 5
vectorA = [0,1,0]
vectorB = [0,-1,0]
angle = Vector.CompassAngle(vectorA, vectorB)
assert angle == 180, "Vector.CompassAngle. Should be 180"

# Case 7 - Coordinates
vectorA = [10,20,30]
# test 1
coordinates = Vector.Coordinates(vectorA, outputType="xyz")
assert coordinates == [10,20,30], "Vector.Coordinates. Should be [10,20,30]"

# test 2
coordinates = Vector.Coordinates(vectorA, outputType="xy")
assert coordinates == [10,20], "Vector.Coordinates. Should be [10,20]"

# test 3
coordinates = Vector.Coordinates(vectorA, outputType="xz")
assert coordinates == [10,30], "Vector.Coordinates. Should be [10,30]"

# Case 8 - Cross
vectorA = [1,0,0]
vectorB = [0,1,0]
cross = Vector.Cross(vectorA, vectorB)
assert cross == [0,0,1], "Vector.Cross. Should be [0,0,1]"

# Case 9 - Up
vector = Vector.Up()
assert vector == [0,0,1], "Vector.Up. Should be [0,0,1]"

# Case 10 - Down
vector = Vector.Down()
assert vector == [0,0,-1], "Vector.Down. Should be [0,0,-1]"

# Case 11 - North
vector = Vector.North()
assert vector == [0,1,0], "Vector.North. Should be [0,1,0]"

# Case 12 - East
vector = Vector.East()
assert vector == [1,0,0], "Vector.East. Should be [1,0,0]"

# Case 13 - South
vector = Vector.South()
assert vector == [0,-1,0], "Vector.South. Should be [0,-1,0]"

# Case 14 - West
vector = Vector.West()
assert vector == [-1,0,0], "Vector.West. Should be [-1,0,0]"

# Case 15 - IsCollinear
# test 1
vectorA = [1,1,1]
vectorB = [10,10,10]
status = Vector.IsCollinear(vectorA, vectorB)
assert status == True, "Vector.IsCollinear. Should be True"

# test 2
vectorA = [1,1,2]
vectorB = [10,10,10]
status = Vector.IsCollinear(vectorA, vectorB)
assert status == False, "Vector.IsCollinear. Should be False"

# Case 16 - Magnitude
# test 1
vectorA = [10,0,0]
magnitude = Vector.Magnitude(vectorA)
assert magnitude == 10, "Vector.Magnitude. Should be 10"

# Case 17 - Multiply
# test 1
vectorA = [10,0,0]
magnitude = 10
vectorB = Vector.Multiply(vectorA, magnitude)
assert vectorB == [100,0,0], "Vector.Multiply. Should be [100,0,0]"

# Case 18 - Normalize
# test 1
vectorA = [10,0,0]
vectorB = Vector.Normalize(vectorA)
assert vectorB == [1,0,0], "Vector.Normalize. Should be [1,0,0]"

# Case 19 - Reverse
# test 1
vectorA = [10,10,0]
vectorB = Vector.Reverse(vectorA)
assert vectorB == [-10,-10,0], "Vector.Normalize. Should be [1,0,0]"

# Case 20 - SetMagnitude
# test 1
vectorA = [10,20,0]
magnitude = 20
vectorB = Vector.SetMagnitude(vectorA, magnitude)
magnitude = Vector.Magnitude(vectorB)
assert magnitude == 20, "Vector.SetMagnitude. Should be 20"
