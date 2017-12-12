#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Cube(object):
	def __init__(self, dimensions=3, colors=['W', 'O', 'G', 'R', 'B', 'Y']):
		self.dimensions = dimensions
		self.colors = colors
		self.sides = [[color for i in range(self.dimensions**2)] for color in self.colors]

	def draw_side(self, side_index):
		horizontal = "───" + "┼───" * (self.dimensions - 1)
		side = ["" for i in range(self.dimensions*2 + 1)]
		side[0] = '┌' + "───" + "┬───" * (self.dimensions - 1) + '┐'
		for y in range(self.dimensions):
			print y
			# for x in range(self.dimensions):
			# side[y] = '│'
			# print y*self.dimensions + x
			side[y*2 + 1] = '│'
			for x in range(self.dimensions):
				side[y*2 + 1] += ' ' + self.sides[side_index][y*self.dimensions + x] + ' │'
			side[y*2 + 2] = '├' + horizontal + '┤'
			if y == self.dimensions - 1:
				side[y*2 + 2] = '└' + "───" + "┴───" * (self.dimensions - 1) + '┘'
		return side


c = Cube(4)
for side in c.draw_side(0):
	print side

