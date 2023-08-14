# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#from connection import *
from functions import *
from niryo_one_tcp_client import *
import numpy as np

if __name__ == '__main__':

    niryo_one_client = NiryoOneClient()

    connectRobot(niryo_one_client)
    calibrate(niryo_one_client)
    moveToPoint(niryo_one_client)



