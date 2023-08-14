
from functions import *
from niryo_one_tcp_client import *


if __name__ == '__main__':

    niryo_one_client = NiryoOneClient()
    # The following user defined functions are declared in functions.py
    connectRobot(niryo_one_client)
    # ensure the Robot is calibrated before move commands are issued.
    calibrate(niryo_one_client)
    # move the Robot through a series of points
    moveToPoint(niryo_one_client)



