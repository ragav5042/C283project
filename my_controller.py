from controller import Robot
from controller import Motor
from controller import Altimeter
import math

class MyController(Robot):
    def __init__(self):
        super(MyController, self).__init__()
        self.timeStep = 32  # set the control time step

        # get device tags
        self.distanceSensor = self.getDevice('ds0')     
        self.distanceSensor.enable(self.timeStep)  # enable sensors to read data from them
        
        self.accelerometer=self.getDevice("accelerometer")
        self.accelerometer.enable(self.timeStep)     
                
         
        self.left_motor = self.getDevice("left wheel motor")
        self.right_motor = self.getDevice("right wheel motor")
        self.left_motor.setPosition(math.inf)
        self.right_motor.setPosition(math.inf)
        
        
        self.left_motor.setVelocity(0.5)
        self.right_motor.setVelocity(-0.5)
        self.direction_switch = True
        self.accValues=[]


    def run(self):
            
        while self.step(self.timeStep) != -1:
            # Get the acceleration vector, which is close the gravity vector.
            # const double *acceleration = wb_accelerometer_get_values(accelerometer)
            # print(self.accelerometer.getValues())
            for i in range(3):
                 self.accValues.append(self.accelerometer.getValues())                          
            
            self.accValues=[]
    
# main Python program
controller = MyController()
controller.run()