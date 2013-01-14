
from bot import *
from vec2d import Vec2d

from pyglet.gl import *
from renderer import renderer, Color


class World:

	def __init__(self):

		self.size = Vec2d(500.0, 500.0)

		self.bots = []


	def add_bot(self, bot):
		self.bots.append(bot)

	def update(self, dt):
		for bot in self.bots:
			bot.update(dt)

	def render(self):

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(-10.0, self.size.x + 10.0, -10.0, self.size.y + 10.0, 100.0, -100.0)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		renderer.set_color(Color.WHITE)
		renderer.rectangle(Vec2d(0.0, 0.0), self.size)

		for bot in self.bots:
			bot.render()



