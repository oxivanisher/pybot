
from pyglet.gl import *


class Color:

	def __init__(self, r, g, b, a):
		self.r = r
		self.g = g
		self.b = b
		self.a = a


Color.BLACK = Color(0.0, 0.0, 0.0, 0.0)
Color.WHITE = Color(1.0, 1.0, 1.0, 1.0)
Color.RED = Color(1.0, 0.0, 0.0, 1.0)

class Renderer:


	def __init__(self):
		self.color = Color.WHITE
		self.fill_color = Color.WHITE

		glDisable(GL_CULL_FACE)


		glLineWidth(10.0)

	def clear(self, color = Color.BLACK):
		glClearColor(color.r, color.g, color.b, color.a)
		glClear(GL_COLOR_BUFFER_BIT)

	def set_color(self, color):
		self.color = color

	def set_fill_color(self, color):
		self.fill_color = color

	def rectangle(self, pos, size):
		glColor4f(self.color.r, self.color.g, self.color.b, self.color.a)
		glBegin(GL_LINE_STRIP)
		glVertex2f(pos.x, pos.y)
		glVertex2f(pos.x + size.x, pos.y)
		glVertex2f(pos.x + size.x, pos.y + size.y)
		glVertex2f(pos.x, pos.y + size.y)
		glVertex2f(pos.x, pos.y)
		glEnd()


renderer = Renderer()