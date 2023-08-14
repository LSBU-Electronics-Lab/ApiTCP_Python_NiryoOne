from niryo_one_tcp_client import *
import variables as v

# user defined function
def connectRobot(niryo_one_client):
    niryo_one_client.connect("10.10.10.10") # connect to the Robot's Wireless Hotspot

# user defined function
def calibrate(niryo_one_client):
    status, data = niryo_one_client.calibrate(CalibrateMode.AUTO) # Robot Calibration Function

#user defined function
def jointsPosition():
    # Robot Joints:  Waist=J1, Shoulder=j2, Elbow=j3, Yaw(Elbow Roll)=j4, Pitch=j5, Roll(Gripper)=j6
    # increment Joint 1 (Waist) by 0.1 rads
    v.J1 = v.J1 + 0.1
    #v.J2 = v.J2 + 0.1
    #v.J3 = v.J3 + 0.1
    #v.J4 = v.J4 + 0.1
    #v.J5 = v.J5 + 0.1
    #v.J6 = v.J6 + 0.1
#   End of function

# user defined function
def moveToPoint(niryo_one_client):

    positionsNumber = 3   # Number of times to increment joint values

    while v.counter <= positionsNumber:  # While loop for 3 times
        # command to move the Robot in Joint Mode
         niryo_one_client.move_joints(v.J1, v.J2, v.J3, v.J4, v.J5, v.J6)
         # move the robot joint by the increment value defined the loop Counter
         v.counter = v.counter + 1
         # Update Robots Joint Positions
         jointsPosition()
         # delay 1 second
         niryo_one_client.wait(1)
    # End of the While loop here on this line.

    # Releasing connection
    # move the Robot to the Sleep Joint Position.
    niryo_one_client.move_joints(*v.sleep_joints)
    # Enable Learning Mode = Release breaks of the Robot joint
    niryo_one_client.set_learning_mode(True)
    # disconnect from Netwrok
    niryo_one_client.quit()


