from Classes import MouseControl
import pigpio

def assert_pwm_load(mouseControl, pwm, load):
    assert(mouseControl.loaded == load)
    assert(mouseControl.pi.get_servo_pulsewidth(mouseControl.pin) == pwm)

if __name__ == '__main__':
    print("we are testing our MouseControl stuff")
    
    #set up individual pins
    pin_val1 = 17
    
    #setup of closed pwm val
    closed_pwm_val1 = 500
    
    print("setting up mouse control instance")
    #set up individual MouseControl instances
    mouseControl1 = MouseControl(pin_val1, closed_pwm_val1)
    
    #make sure MouseControl pin is the value passed in
    assert(mouseControl1.pin == pin_val1)
    
    #call release mouse
    mouseControl1.release_mouse()

    #check pulsewidth and loaded state
    assert_pwm_load(mouseControl1, 1500, False)
    
    #call reset
    mouseControl1.reset()
    
    #check pulsewidth and loaded state
    assert_pwm_load(mouseControl1, closed_pwm_val1, True)
    
    print("Done Testing")