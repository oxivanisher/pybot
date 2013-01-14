
import math
from vec2d import Vec2d

from pyglet.gl import *
from renderer import renderer, Color

class Bot:

	def __init__(self, controller):

		self.controller = controller

		self.position = Vec2d()
		self.angle = 0.0
		self.angle_speed = 5.0
		self.target = Vec2d()
		self.velocity = Vec2d()

	def update(self, dt):
		#self.angle += 1.0 * dt

		d = self.target - self.position
		d = d.normalized()
		target_angle = d.get_angle()

		print target_angle

		#self.angle = target_angle
		if self.angle < target_angle:
			self.angle += dt * self.angle_speed
		else:
			self.angle -= dt * self.angle_speed


		d = Vec2d(math.cos(self.angle), math.sin(self.angle))

		d *= dt * 100.0

		self.position += d

	def render(self):

		glPushMatrix()

		# Position bot in world
		glTranslatef(self.position.x, self.position.y, 0.0)

		# Rotate bot on position
		glRotatef(self.angle / math.pi * 180.0, 0.0, 0.0, 1.0)

		# Move to local origin
		glTranslatef(-5.0, -5.0, 0.0)

		renderer.rectangle(Vec2d(), Vec2d(10.0, 10.0))
		renderer.rectangle(Vec2d(1.0, 1.0), Vec2d(8.0, 8.0))
		renderer.rectangle(Vec2d(2.0, 2.0), Vec2d(6.0, 2.0))

		glPopMatrix()



		pass


class BotController:

	def fire(self):
		pass

	def update(self):
		pass

	pass