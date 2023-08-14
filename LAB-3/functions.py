from niryo_one_tcp_client import *
import variables as v
import numpy as np

def connectRobot(n1):

    status=n1.connect("10.10.10.10")
    n1.change_tool(v.gripper_used)
    n1.open_gripper(v.gripper_used, v.gripper_speed)
    print("Connection to robot successful\nGripper attached ")

def calibrate(n1):

       status, data = n1.calibrate(CalibrateMode.AUTO)
       n1.move_joints(*v.sleep_joints)
       n1.set_learning_mode(True)
       print("Robot calibrated and in initial position")

def learningMode(n1):
#Begining of Learning/Teach Mode

    status, data1 = n1.set_learning_mode(True)
    # Ensure the robot joint coordinate arrays are deleted from the list
    # CAUTION !! every time you run the learning mode the previous taught poistions are deleted
    del np.joints[:]
    print("-------Learning Mode----------- ")
    # In this mode pressing s - stores the position with the gripper remaining OPEN
    # pressing g - stores the positions with the gripper CLOSED

    # This while loop ends either by pressing 'q' or when all points are taught
    # defined by the maximum value of number_Of_positions (declared in variables.py)
    while v.keyPressed != 'q':

        v.keyPressed = input(" Press s+ENTER for open gripper position"
                             "\n Press g+ENTER for close gripper position"
                             "\n Press q+ENTER to quit\n  ")

        if v.keyPressed in  ['s','g']:
            if v.i < v.number_Of_positions:
                # get the joint coordinates of the Robot and store them in data2 array
                status, data2 = n1.get_joints()
                # depending on Gripper status insert 0 for OPEN and 1 for CLOSE Gripper in
                # array position 6
                data2.insert(6,0)
                if v.keyPressed == 'g':
                    data2[6]= 1
                # point to the next joint array position by appending data to it
                np.joints.append(data2)
                v.i = v.i + 1
                print("Positions in radians: [j1,j2,j3,j4,j5,j6,gripper],[j1,j2....second position],[...]etc ")
                print(np.joints)
                print("Number of positions %d " % len(np.joints))

                # check the total number of positions are taught, then stop
                if v.i == v.number_Of_positions:
                   print("Taught points maximum value is reached")
                   break # break out of the while loop if all points are Taught
# end of the WHILE LOOP

def repeatMode(n1,joints):
# extract the joints one point at a time from the stored list and move to the coordinates
        for i in range (len(joints)):
            print("[j1,            j2,             j3,            j4,            j5,              j6,           gripper 0-Open 1-Closed]")
            print(joints[i][0], joints[i][1], joints[i][2], joints[i][3], joints[i][4], joints[i][5], joints[i][6])
            n1.move_joints(joints[i][0], joints[i][1], joints[i][2], joints[i][3], joints[i][4], joints[i][5])

            if joints[i][6] == 0:
            # check the array's 6th position to detect the Gripper FLAG
            # if the flga is 1 CLOSE gripper of 0 then OPEN Gripper
                  n1.open_gripper(v.gripper_used, v.gripper_speed)
            else:
                   n1.close_gripper(v.gripper_used, v.gripper_speed)
            # wait for 2 senconds
            n1.wait(v.position_delay)


        n1.move_joints(*v.sleep_joints)
        n1.set_learning_mode(True)
        print("Repeat mode ended")
