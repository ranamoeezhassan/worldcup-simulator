'''physics_objects.py

Rana Moeez Hassan
CS 152 A
Project 8
11/15/22

This program defines the parent class and the three subclasses that are used
in other files.

The program outputs nothing so there is no point to running this file.
This file was developed with the intention of this being a module that we 
can import'''
import graphicsPlus as gr #importing modules

class Thing(object):
    '''Parent class for all simulated objects'''
    def __init__(self, win, the_type):
        self.type = the_type #defining the variables
        self.mass = 1
        self.position = [0 , 0]
        self.velocity= [0, 0]
        self.acceleration = [0, 0]
        self.elasticity = 1
        self.scale = 10
        self.win = win
        self.vis = []
        self.color = None
        self.drawn = bool(False)
    
    def getType(self):
        return self.type

    def getPosition(self):
        '''This function returns the position of the center of the object'''
        return tuple(self.position[:])

    def getVelocity(self):
        '''This function returns the velocity of the ball'''
        return tuple(self.velocity[:])

    def getAcceleration(self):
        '''This function returns the acceleration of the ball'''
        return tuple(self.acceleration[:])

    def getMass(self): 
        '''This function returns the mass of the ball'''
        return float(self.mass)

    def draw(self):
        '''This function draws the shape into the window'''
        vis = self.vis
        win = self.win
        for i in vis: #draw each shape in the list into the window
            i.draw(win)
        self.drawn = bool(True)

    def undraw(self):
        '''This function undraws the object from the window'''
        vis = self.vis
        for shape in vis: #undraw each shape in the list from the window
            shape.undraw()
        self.drawn = bool(False)

    def setVelocity(self, vx, vy):
        '''This function sets the x and y velocities given to it as the new velocity of the object'''
        self.velocity = [vx, vy]

    def setAcceleration(self, ax, ay):
        '''This function sets the x and y acceleration given to it as the new acceleration of the ball'''
        self.acceleration = [ax, ay]
    
    def setMass(self, mass_new):
        '''This function sets the mass of the object'''
        self.mass = mass_new
    
    def setElasticity(self, elasticity_new):
        '''This function sets the elasticity of the ball'''
        self.elasticity = elasticity_new
    
    def getElasticity(self):
        ''''This function gets the elasticity of the ball'''
        return self.elasticity

    def setPosition(self, px, py):
        '''This function sets the coordiantes given to it as the new coordiantes of the object'''
        point = self.getPosition() #getting the coordinates of the ball
        x_old = point[0]
        y_old = point[1]
        self.position = [px, py]
        newpoint = self.getPosition()
        dx = (newpoint[0] - x_old) * self.scale #finding the "steps" we need to take in respective direction
        dy = (newpoint[1] - y_old) * self.scale
        for item in self.vis:
            item.move(dx, dy) #moving each object in the list with the respective "steps"
    
    def setColor(self, c):
        '''This function takes in a rgb tuple and changes the colour of the object'''
        self.color = c 
        color = gr.color_rgb(c[0], c[1], c[2])
        if c != None:
            for each in self.vis:
                each.setFill(color)

    def update(self, dt):
        '''This function updates the x and y coordinates of the ball considering one of the SUVAT equations
        to model the motion of the ball under a constant acceleration'''
        point = self.getPosition() #getting the variables that we need
        vel = self.getVelocity()
        acc = self.getAcceleration()
        x_old = point[0] # assign to x_old the current x position
        y_old = point[1] # assign to y_old the current y position
        x_vel = vel[0]
        y_vel = vel[1]
        x_acc = acc[0]
        y_acc = acc[1]
        update_x_pos = x_old + x_vel * dt + 0.5 * x_acc * dt * dt # update the x position to be x_old + x_vel*dt + 0.5*x_acc * dt*dt
        self.position[0] = update_x_pos
       
        update_y_pos = y_old + y_vel * dt + 0.5 * y_acc * dt * dt  # update the y position to be y_old + y_vel*dt + 0.5*y_acc * dt*dt
        self.position[1] = update_y_pos
        dx = (update_x_pos - x_old) * self.scale # assign to dx the change in the x position times the scale factor (self.scale)
        dy = (update_y_pos - y_old) * -1 * self.scale # assign to dy the negative of the change in the y position times the scale factor (self.scale)
        for item in self.vis:  # for each item in self.vis
            item.move(dx, dy) # call the move method of the graphics object with dx and dy as arguments..
        update_x_vel = x_acc * dt + x_vel # update the x velocity by adding the acceleration times dt to its old value
        self.velocity[0] = update_x_vel  
        update_y_vel = y_acc * dt + y_vel # update the y velocity by adding the acceleration times dt to its old value
        self.velocity[1] = update_y_vel

class Ball(Thing):
    '''Subclass that inherits the parent class "Thing" and its attributes/methods. This class also defines the specific 
    methods for the ball class'''
    def __init__(self, win, radius = 1):
        Thing.__init__(self, win, "ball") #defining the variables
        self.radius = radius
        self.refresh()
        self.setColor((0, 0, 0))

    def refresh(self):
        '''This function refreshes the visualization of the object'''
        drawn = self.drawn
        if drawn:
            self.undraw() #undrawing the object
        self.vis = [gr.Circle(gr.Point(self.position[0]*self.scale, self.win.getHeight() - self.position[1]*self.scale), self.radius*self.scale)]
        if drawn:
            self.draw() #drawing the object
    
    def getRadius(self):
        '''This function gets the radius of the object'''
        return float(self.radius)
    
    def setRadius(self, r):
        '''This function sets the radius of the object'''
        self.radius = r
        self.refresh()

class Block(Thing):
    '''Subclass that inherits the parent class "Thing" and its attributes/methods. This class also defines the specific 
    methods for the block class'''
    def __init__(self, win, x0 = 0, y0 = 0, width=2, height= 1): #color= (0,0,0)):
        Thing.__init__(self, win, "block")
        self.x0 = x0    #defining the variables
        self.y0 = y0
        self.position = [x0, y0]
        self.width = width
        self.height= height
        self.reshape()
        #self.setColor(color)
    
    def reshape(self):
        '''This function visualizes the object'''
        drawn = self.drawn
        if drawn:
            self.undraw() #undraws the object if it is drawn
        self.vis = [gr.Rectangle(gr.Point((self.position[0] - self.width/2 )* self.scale, (self.position[1] - self.height/2) * self.scale), 
        gr.Point((self.position[0] + self.width/2 )*self.scale, (self.position[1] + self.height/2 )* self.scale))]
        if drawn:
            self.draw() #drawing the object back

    def getWidth(self):
        '''This function gets the width of the block'''
        return self.width

    def getHeight(self):
        '''This function gets the height of the block'''
        return self.height
    
    def setWidth(self, dx):
        '''This functiom sets the width of the block'''
        self.width = dx
        self.reshape()
    
    def setHeight(self, dy):
        '''This function sets the height of the block'''
        self.height = dy
        self.reshape()

class Triangle(Thing):
    '''Subclass that inherits the parent class "Thing" and its attributes/methods. This class also defines the specific 
    methods for the triangle class'''
    def __init__(self, win, x0 = 0, y0 = 0 , width =10 , height = 3, color= (0,0,0)):
        Thing.__init__(self, win, "triangle")
        self.position = [x0, y0] #defining the variables
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
        self.reshape()
        self.setColor(color)

    def reshape(self):
        '''This function visualizes the object'''
        drawn = self.drawn
        if drawn:
            self.undraw()  #undraws the object if it is drawn
        self.vis = [gr.Polygon(gr.Point(self.position[0] *self.scale ,self.win.getHeight() - (self.position[1] + self.height/2) * self.scale), 
        gr.Point((self.position[0] + self.width/2) *self.scale , self.win.getHeight() - ((self.position[1] - self.height/2 )* self.scale)),
        gr.Point((self.position[0] - self.width/2) *self.scale ,self.win.getHeight() - ((self.position[1] - self.height/2 )* self.scale)))]
        #visualizing the object
        if drawn:
            self.draw() #drawing the object back
    
    def getWidth(self):
        '''This function gets the width of the block'''
        return self.width

    def getHeight(self):
        '''This function gets the height of the block'''
        return self.height
    
    def setWidth(self, dx):
        '''This function sets the width of the block'''
        self.width = dx
        self.reshape()
    
    def setHeight(self, dy):
        '''This function sets the height of the block'''
        self.height = dy
        self.reshape()

class Unique_object(Thing):
    '''Subclass that inherits the parent class "Thing" and its attributes/methods. This class also defines the specific 
    methods for the a unique object class. The object is treated as a ball in order to simplify collisions'''
    def __init__(self, win, x0 = 0, y0 = 0 , width =10 , height = 3,radius = 3, color= (0,0,0)):
        Thing.__init__(self, win, "ball")
        self.position = [x0, y0] #definig the variables
        self.x0 = x0
        self.y0 = y0
        self.radius = radius
        self.width = width
        self.height = height
        self.reshape()
        self.setColor(color)

    def reshape(self):
        drawn = self.drawn
        if drawn:
            self.undraw()  #undraws the object if it is drawn
        self.vis += [gr.Polygon(gr.Point(self.position[0] *self.scale ,self.win.getHeight() - (self.position[1] + self.height/2) * self.scale), 
        gr.Point((self.position[0] + self.width/2) *self.scale , self.win.getHeight() - ((self.position[1] - self.height/2 )* self.scale)),
        gr.Point((self.position[0] - self.width/2) *self.scale ,self.win.getHeight() - ((self.position[1] - self.height/2 )* self.scale))),
        gr.Circle(gr.Point((self.position[0] + self.width/2)*self.scale, self.win.getHeight() - (self.position[1] + self.height/2 )*self.scale), self.radius*self.scale),
        gr.Circle(gr.Point((self.position[0] - self.width/2)*self.scale, self.win.getHeight() - (self.position[1] + self.height/2 )*self.scale), self.radius*self.scale),
        gr.Rectangle(gr.Point((self.position[0] - self.width/2 )* self.scale, self.win.getHeight() - (self.position[1] - self.height/2) * self.scale), 
        gr.Point((self.position[0] + self.width/2)* self.scale,self.win.getHeight() - (self.position[1] - self.height*3/2 )* self.scale))] #visualizing the object
        # self.vis = [gr.Polygon(gr.Point(0, 0), gr.Point(10, 10), gr.Point(10,20))]
        if drawn:
            self.draw() #drawing the object back 
    
    def getRadius(self):
        '''This function gets the radius of the object'''
        return float(self.radius)
    
    def setRadius(self, r):
        '''This function sets the radius of the object'''
        self.radius = r
        self.reshape()