from niryo_one_tcp_client import *
import numpy as np

gripper_used = RobotTool.GRIPPER_1  # SERVO based Gripper
gripper_speed = 1000  # max speed 1000
sleep_joints = [0.0, 0.55, -1.2, 0.0, 0.0, 0.0]  # joint positions when Robot is calibrated
counter = 0

# default SAFE joint positions
J1 = -1.5
J2 = 0.0
J3 = 0.0
J4 = 0.0
J5 = 0.0
J6 = 0.0
i = 0

option='' # menu option
keyPressed= "" # Learning/Teach mode option

# maximum number of positions to Teach/Learn
number_Of_positions = 6
# array of taught positions
np.joints = []
# delay in SECs at each position reached
position_delay = 2