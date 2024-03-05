import os

startWeb = 0


def startWebServer():
    print("\n\n\t\t ---->>\tSTARTING YOUR APACHE WEB SERVER\t<----\t\t\n\n")
    os.system("systemctl start httpd")
    print("\n\n\t\t ---->>\tWEB SERVER STATUS\t<----\t\t\n\n")
    print("\n\tEnter ---> :q or [ ctrl+c ]<----  to exit\n\n")
    os.system("systemctl status httpd")
    os.system("systemctl stop firewalld")
    startWeb = 1
    return


def hostWebSite():
    print("\n\n\t\tWELCOME TO WEB HOSTING\t\t\n\n")
    fileName = input("Enter your file name : ")
    fileNameHTML = fileName + '.html'
    os.system("ifconfig enp0s3")
    ip = input("\n\tFor confirmation Enter the ip address : ")
    choice = 'y'
    while (choice == 'y'):
        print("\n\t Enter your html code inside the display\n")
        print("Press ' i ' to edit and ' esc + :wq ' to save your program")
        os.system("sleep 5")
        os.system("vi /var/www/html/{}".format(fileNameHTML))
        print("\n\t\tyou have succesfully created your  html file \n")
        choice = input("\n\t DO you want to edit the html file [y/n] : ")
    print("\n\t\tGENERATING URL")
    os.system("sleep 3")
    urlGenerator(ip,fileNameHTML)
    return

#the prepend_line() function will allow to make neccessary 
#changes to the python file to make it readable for the web browser
def prepend_line(file_name, list_of_lines):
    """Insert given list of strings as a new lines at the beginning of a file"""
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open given original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Iterate over the given list of strings and write them to dummy file as lines
        for line in list_of_lines:
            write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)
    return file_name





# here we will convert the api file on the host
def configureApi():
    print("HERE WE WILL HOST API")
    os.system("ifconfig enp0s3")
    ipAddress = input("\n\tFor confirmation Enter the ip address : ")
    ip = ipAddress + '/cgi-bin'
    userFileName = input("Enter your file name : ")
    print("\n\tOPENING {} FILE \t\n".format(userFileName))
    print("\n\tEnter your python code\t\n\n")
    os.system("sleep 5")
    fileName = userFileName +'.py'
    extraLines = ['#! usr/bin/python3','print("content-type : text/html")']
    modifiedFileName = prepend_line(fileName,extraLines)
    

    os.system("vi /var/www/cgi-bin/{}".format(modifiedFileName))
    os.system("chmod +x /var/www/cgi-bin/{}".format(modifiedFileName))
    urlGenerator(ip,modifiedFileName)
    return

def urlGenerator(ip,fileName):
    print("\n\n\t\tBELOW IS YOUR URL \n\n")
    print("\n\t\t------>\t http://{}/{}".format(ip,fileName))



# --------------------------->>> MENU2 ()  <<-------------------

def menu2():
    reEnter = 'y'
    while(reEnter == 'y'):
            ch = input(
               "\n\n\t\tENTER 1 TO HOST A FILE\nENTER 2 TO CONFIGURE AN API")
            if(ch == 1):
                hostWebSite()

            elif(ch == 2):
                configureApi()

            else:
                print("\n\tYOU HAVE ENTERED WRONG CHOICE\n")
            reEnter = input("\n\tDO YOU WANT TO CONTINUE [y/n] : ")


# --------------------------->>> MENU ()  <<-------------------

def menu():
    os.system("clear")
    webInstalled = input(
        "\n\n\nDo you have apache web server installed [y/n] : ")

    if(webInstalled == 'y'):
        startWebServer()
        menu2()

    else:
        print("\n\n\t\t ---->>\tINSTALLING APACHE SERVER\t<----\t\t\n\n")
        os.system("dnf install httpd")
        print("\n\n\t\t ---->>\tAPACHE WEB SERVER INSTALLED\t<----\t\t\n\n")
        startWebServer()
        menu2()
