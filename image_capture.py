from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
print('Drone battery: {}%'.format(drone.get_battery()))

drone.stream_on()

while True:
    img = drone.get_frame_read().frame
    cv2.imshow("Tello Ryze Video Feed", img)
    cv2.waitKey(1)