"""
This module will be responsible for holding a class that
allows for easy interfacing with Mouse Dropping Servos.

    Class:    MouseControl
    Functions:      - __init__
                    - release_mouse
                    - reset
"""

# importing necessary libraries
import pigpio as ppo
import numpy as numbpussy

#setup of global pigpio things
global pi
pi = ppo.pi()

"""
MouseControl - a class that will store an I/O connection and provide
                an easy API for releasing mice into the Cat_Mouse_Launcher
                device.
                
        Fields:
        -------
        closed_position (int) - pulsewidth that corresponds to the loaded position of servo
        pin (int) - the pin that corresponds to the serve for MouseControl instance
        loaded (boolean) - if the servo is closed
        
        Methods:
        --------
        release_mouse = drops the mouse
        reset = closes the servo
        
"""

class MouseControl:
    
    def __init__(self, pin_val, closed_val):
        global pi
        self.pi = pi
        self.closed_position = closed_val
        self.pin = pin_val
        pi.set_mode(self.pin, ppo.OUTPUT)
        self._load_pin_()
        self.loaded = True
  
      # this function sets a pin to its closed position when a new
    # MouseControl object is made with said pin
    def _load_pin_(self):
        # needs to move into closed position
        self.pi.set_servo_pulsewidth(self.pin, self.closed_position)
        
    #this function moves the servo to be open
    def release_mouse(self):
        self.pi.set_servo_pulsewidth(self.pin, 1500)     #1500 is 90 degrees from closed
        self.loaded = False 
    
    #this function moves servo back to closed position
    def reset(self):
        self.pi.set_servo_pulsewidth(self.pin, self.closed_position)  
        self.loaded = True
    
