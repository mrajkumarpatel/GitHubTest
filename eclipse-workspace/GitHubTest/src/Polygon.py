'''
Created on 24-Jul-2019

@author: Raj
'''

import math


class Polygon:
	def __init__(self, size, circum_radius):
		if size < 3:
			raise ValueError(
				"Cannot Form a Polygon with size/number of edges less than 3. "
				"Atleast 3 edges are required to make a polygon.")
		self.size = size
		self.number_of_vertices = size
		self.number_of_edges = size
		self.circum_radius = circum_radius
		self.interior_angle = (self.number_of_vertices - 2) * (180 / self.number_of_vertices)
		self.edge_length = 2 * self.circum_radius * math.sin(math.pi / self.number_of_vertices)
		self.apothem = self.circum_radius * math.cos(math.pi / self.number_of_vertices)
		self.area = (1 / 2) * self.number_of_vertices * self.edge_length * self.apothem
		self.perimeter = self.number_of_vertices * self.edge_length

	def __repr__(self):
		return f'Polygon(size={self.number_of_vertices}, circum_radius={self.circum_radius})'

	def __gt__(self, other):
		if isinstance(other, Polygon):
			return self.number_of_vertices > other.number_of_vertices
		else:
			NotImplemented

	def __eq__(self, other):
		if isinstance(other, Polygon):
			return self.number_of_vertices == other.number_of_vertices & self.circum_radius == other.circum_radius
		else:
			NotImplemented

	def print_all_properties(self):
		print("=======================================================================================================\n"
			f"Following are the properties of Polygon - {self.__repr__()}\n\tSize: {self.size}\n\tNumber of Vertices: "
			f"{self.number_of_vertices}\n\tNumber of Edges: {self.number_of_edges}\n\tCircum Radius: {self.circum_radius}"
			f"\n\tInterior Angle: {self.interior_angle}\n\tEdge Length: {self.edge_length}\n\tApothem: "
			f"{self.apothem}\n\tArea: {self.area}\n\tPerimeter: {self.perimeter}\n"
			"=======================================================================================================")


P1 = Polygon(1, 100)
P1.print_all_properties()


P2 = Polygon(4, 100)
print(P2.print_all_properties())

print("P1>P2: ", P1 > P2)
print("P1<P2: ", P1 < P2)
print("P1=P2: ", P1 == P2)
print("P1=Int: ", P1 == int)

