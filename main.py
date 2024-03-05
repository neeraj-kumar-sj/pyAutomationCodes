import os
import Docker_automation as da
import WebServer_automation as wsa
import Linux_Automation as la
import Hadoop_Automation as ha
import Machine_Learning as ml
#import AWS_Automation as aws
os.system("clear")
#os.system("tput setaf 3")

print("\t\t\t\tWelcome welcome welcome\t\t\n\n")

#os.system("tput setaf 5")

print("\n\n\t\t\t\tWelcome to my menu program")


def configureLinux():
    m = """
Press  1: To create a partition
Press  2: To format the disk
Press  3: To mount the disk
Press  4: To configure yum
Press  5: To configure apache web server
Press  6: To create a Lvm Storage
"""

    exitStatus = 'yes'
    while(exitStatus == 'yes'):
        print(m)

        ch = input("Input Your Choice: ")
        if (ch == '1'):
            la.create_partition()

        elif(ch == '2'):
            la.format_disk()

        elif(ch == '3'):
            la.mount_disk()

        elif(ch == '4'):
            la.configure_yum()

        elif(ch == '5'):
            la.configure_appache_web_server()

        elif(ch == '6'):
            la.create_lvm_storage()

        else:
            print("\n\t\tYOU HAVE ENTERED WRONG OPTION \n")

        exitStatus = input("\n\t\tDO YOU WANT TO CONTINUE [yes/no]\t:  ")

    return


def configureAWS():
    print("\n\t\tconfiguring AWS\n\n")
#    aws.awsConfigurationOption()
    return


def configureDocker():
    da.docker()
    return


def configureHadoop():
    m = """
Press  1: To create a namenode on hadoop
Press  2: To create a datanode on hadoop
Press  3: To create a client on hadoop
press  4: To Install Hadoop on the system
"""
    exitStatus = 'yes'
    while(exitStatus == 'yes'):
        print(m)
        ch = input("Input Your Choice: ")
        if(ch == '1'):
            ha.create_namenode_hadoop()

        elif(ch == '2'):
            ha.create_datanode_hadoop()

        elif(ch == '3'):
            ha.create_hadoop_client()

        elif(ch == '4'):
            ha.install_hadoop()

        else:
            print("\n\t\tYOU HAVE ENTERED WRONG OPTION \n")

        exitStatus = input("\n\t\tDO YOU WANT TO CONTINUE [yes/no]\t:  ")

    return


def useMachineLearning():

    print("\n\t\tYou have chosen machine learning\n")
    ml.machineLearningOption()
    return


def menu():
    m = """
Press  1: To configure Linux
Press  2: To Configure AWS
Press  3: To Configure Docker
Press  4: To configure Hadoop
Press  5: To use Machine Learning
Press  6: To Configure Web Server
"""
    print("\n\n\t\t\t\t MAIN MENU \n\n\n")
    exitStatus = 'yes'
    while(exitStatus == 'yes'):

        print(m)
        ch = input("Input Your Choice: ")
        if ch == '1':
            configureLinux()

        elif(ch == '2'):
            configureAWS()

        elif(ch == '3'):
            configureDocker()

        elif(ch == '4'):
            configureHadoop()

        elif(ch == '5'):
            useMachineLearning()

        elif(ch == '6'):
            wsa.menu()
            #this menu will take the user to the Webserver_automation.py file

        else:
            print("\n\t\tYOU HAVE ENTERED WRONG OPTION \n")

        exitStatus = input(
            "\n\t\tDO YOU WANT TO Restart MAIN MENU [yes/no]\t:  ")

    return


print("Do you want to run? Local/Remote")

ch2 = input("l-local and r-remote: ")

if ch2 == 'l':
    exitStatus = 'yes'
#    while(exitStatus == 'yes'):
    menu()
#        exitStatus = input("\n\t\tDO YOU WANT TO CONTINUE [yes/no]\t:  ")


#  does not work for aws as it requires passkey <<-- needs to be taken care of


elif(ch2 == 'r'):
    imp3 = input("Enter the target's IP: ")

    os.system("scp /root/arth_projects/menu1.py "+imp3+":/root")

    os.system("(echo 'l' ; echo &ch) | ssh "+imp3+" python3 menu1.py")

else:
    print("\n\t\tYOU HAVE ENTERED WRONG OPTION \n")
