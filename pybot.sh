import pyglet                                                                      
from pyglet.gl import *                                                            

window = pyglet.window.Window(resizable=True)                                      

@window.event                                                                      
def on_draw():                                                                     
    window.clear()                                                                 
    pyglet.gl.glColor4f(1.0,0,0,1.0)                                               
    glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)                             
    glEnable (GL_BLEND)                                                            
    glEnable (GL_LINE_SMOOTH);                                                     
    glHint (GL_LINE_SMOOTH_HINT, GL_DONT_CARE)                                     
    glLineWidth (3)                                                                
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,                                    
        ('v2i', (10, 15, 300, 305))                                                
    )                                                                              

pyglet.app.run() 