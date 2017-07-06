#CameraTimeLapse.py

import subprocess
import time
from picamera import PiCamera

camera = PiCamera()

def main():
	for i in range(10):
		time.sleep(2)
		camera.capture('image%s.jpg' % i)
		print("\ntaking a picture\n")


if __name__=="__main__":
    main()