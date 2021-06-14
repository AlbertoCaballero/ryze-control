from djitellopy import tello
from modules.keyboard_control_module import KeyboardControll

kp = KeyboardControll()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def control_loop():
    lr, fb, ud, yv = 0, 0, 0, 0
    battery = drone.get_battery()
    speed = 50

    if kp.get_key('e'): 
        drone.takeoff()
    if kp.get_key('q'): 
        drone.land()

    if kp.get_key('a'): 
        lr = -speed
    if kp.get_key('d'): 
        lr = speed

    if kp.get_key('w'): 
        fb = speed
    if kp.get_key('s'): 
        fb = -speed

    if kp.get_key('UP'): 
        ud = speed
    if kp.get_key('DOWN'): 
        ud = -speed

    if kp.get_key('LEFT'): 
        yv = -speed
    if kp.get_key('RIGHT'): 
        yv = speed
    
    print('BT: {} FB: {} LR: {} UD: {} YV: {}'.format(battery, fb, lr, ud, yv))
    drone.send_rc_control(lr, fb, ud, yv)

def main():
    while True:
        control_loop()

if __name__ == '__main__':
    main()
