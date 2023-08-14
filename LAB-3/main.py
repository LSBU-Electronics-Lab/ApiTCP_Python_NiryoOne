
from functions import *
from niryo_one_tcp_client import *

def main():

    print(" Niryo 1 Robot Control Program")
    # Connect to the Robot Wireless Hotspot
    n1 = NiryoOneClient()
    connectRobot(n1)
    # Calibrate the Robot
    calibrate(n1)

# Main Program Loop to Teach/Learn or Repeat a stored sequence
    while v.option !='3':

        print("1. Learning/Teach Mode"
              "\n2. Repeat Mode"
              "\n3. Exit Program")
        v.option=input("Enter Choice: ")
        if v.option == '1':
            print('Learning/Teach Mode')
            learningMode(n1)

        elif v.option =='2':
            print('Repeat Mode')
            repeatMode(n1, np.joints)

        elif v.option =='3':
            print(" Exited Program")
            exit()

# End of While option

if __name__ == '__main__':
    main()











