from djitellopy import tello

class Control:
    speed = 50
    drone = tello.Tello()
    def __init__(self) -> None:
        try:
            self.drone.connect()
            print(self.drone.get_battery())
        except:
            print("Ryze Drone Conection Error")

    def set_speeds(self, lr, fb, ud, yv):

        if ud == 1:
            self.takeoff()
        elif ud == -1:
            self.land()

        if lr == 1 | -1 | 0:
            lr = self.speed * lr
            # lr = round(self.speed * round(lr, 1), 0)
        elif fb == 1 | -1 | 0:
            fb = self.speed * fb
            # fb = round(self.speed * round(fb, 1), 0)
        elif yv == 1 | -1 | 0:
            yv = self.speed * yv
            # yv = round(self.speed * round(yv, 1), 0)

        self.drone.send_rc_control(lr, fb, ud, yv)

    def takeoff(self):
        self.drone.takeoff()

    def land(self):
        self.drone.land()