import pyglet
from pyglet.gl import *
from pyglet import clock

from vec2d import Vec2d
from renderer import renderer

from bot import Bot
from world import World
from simple_controller import SimpleController

class Game:


    def __init__(self):

        self.init_window()

        self.world = World()
        self.bot = Bot(SimpleController())
        self.bot.position = self.world.size * 0.5
        self.world.add_bot(self.bot)

        clock.schedule(self.update)

    def init_window(self):
        config = pyglet.gl.Config(sample_buffers=1, samples=4)
        self.window = pyglet.window.Window(config=config, resizable=True) 
        self.window.set_size(1024, 768)

        self.window.on_draw = self.on_draw
        self.window.on_mouse_press = self.on_mouse_press

    def update(self, dt):
        self.world.update(dt)


    def run(self):
        pyglet.app.run()

    def on_draw(self):

        self.window.clear()                                                                 
        self.world.render()

        # pyglet.gl.glColor4f(1.0,0,0,1.0)                                               
        # glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)                             
        # glEnable (GL_BLEND)                                                            
        # glEnable (GL_LINE_SMOOTH);                                                     
        # glHint (GL_LINE_SMOOTH_HINT, GL_DONT_CARE)                                     
        # glLineWidth (3)                                                                
        # pyglet.graphics.draw(2, pyglet.gl.GL_LINES,                                    
        #     ('v2i', (10, 15, 300, 305))                                                
        # )                                                                              

    def on_mouse_press(self, x, y, button, modifiers):
        self.bot.target.x = (float(x) / self.window.width) * 520.0 - 10.0
        self.bot.target.y = (float(y) / self.window.height) * 520.0 - 10.0
        #self.bot.position = self.bot.target
        print self.bot.target
        pass