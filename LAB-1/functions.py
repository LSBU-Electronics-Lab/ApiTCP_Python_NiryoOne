from niryo_one_tcp_client import *
import variables as v

def connectRobot(niryo_one_client):

    niryo_one_client.connect("10.10.10.10")


def calibrate(niryo_one_client):

    status, data = niryo_one_client.calibrate(CalibrateMode.AUTO)
    print('status=',status)
    print('data=',data)
def moveToPoint(niryo_one_client):



    niryo_one_client.move_joints(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

    niryo_one_client.change_tool(v.gripper_used)

    niryo_one_client.close_gripper(v.gripper_used, v.gripper_speed)

    niryo_one_client.open_gripper(v.gripper_used, v.gripper_speed)

    niryo_one_client.move_joints(*v.sleep_joints)
    niryo_one_client.set_learning_mode(True)
    # Releasing connection
    niryo_one_client.quit()