from manim import *
import math
import numpy as np
import random
colors = [RED,ORANGE,YELLOW,GREEN,BLUE,PURPLE]
class Video(MovingCameraScene):
    def construct(self):
        # self.play(self.camera.frame.animate.set(width=2.8).move_to([0,1.75,0]),run_time=0.01)
        # dot = Circle(radius = 0.05, color=RED)
        # # dot.position_update = [random.randint(3, 9), random.randint(3, 9), 0]
        # dot.x = -1.41
        # dot.y = 0.1
        # def update_xy(mob):
        #     mob.x, mob.y = mob.x+0.1, math.sqrt(abs(2-mob.x**2))
        # P1=Pendulum(0.3)
        # dot=Circle(radius = 0.05, color = RED)
        # dot.OBJ = P1
        obs=[]
        
        def update_position(ob,dt):
            ob.PENDULUM.update_object(dt)
            ob.move_to(ob.PENDULUM.position)
            ob.LINE.put_start_and_end_on([0,0,0], ob.PENDULUM.position)

        for i in range(2, 7):
            p = Pendulum(i/4)
            dot=Circle(radius = 0.05, color = colors[i%6]).set_fill(colors[i%6])
            dot.PENDULUM = p 
            line = Line(start=[0,2,0],end=dot.PENDULUM.position,stroke_width=0.5)
            dot.LINE = line
            dot.add_updater(update_position)
            obs.append(dot)
        for i in obs:
            self.add(i)
            self.add(i.LINE)
        self.update_self(0)
        self.wait(5)	    
	    

class Pendulum: 
    def __init__(self,length):
        self.max_amplitude = math.radians(90)
        self.length = length
        self.scaling = 2.0
        self.offset = 0.0

        self.position_offset = np.array([0.0,2.0,0.0])
        self.position = np.array([0.0,0.0,0.0]) 
        self.time = 0
        dt=0.0
        self.phase = 0

    def update_object(self,dt):
        self.time += dt
        period = 2 * math.pi * math.sqrt(self.length/9.8)
        theta = self.max_amplitude * math.cos(2 * math.pi / period * self.time + self.offset)
        x,y = self.length*self.scaling * math.sin(theta),0 - (self.length*self.scaling * math.cos(theta))
        self.position = np.array([x,y,0.0]) + self.position_offset
        self.phase = self.time / period
        