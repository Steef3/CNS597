#NOTE:
# auth.log is needed, which is just a regular log file

import os

'''
print(os.name)

def MOVE():
    print("You are in the directory:{}".format(os.getcwd()))
    print("Directory {} contains:".format(os.getcwd())
    for item in os.listdir():
        print(item)

    ans = input("Would you like to change directories?")
    if ans.lower() == 'yes':
        dirAns = input("What directory would you like to change to?")
        os.dir(dirAns)
    elif ans.lower() == 'no':
        pass
    else:
        print("Invalid response, please try again.")

MOVE()
'''

def FIND_CONFIGS():
    # OS version
    print("This is the OS version:")
    print(os.system("hostnamectl"))
    # lsb_release -a
    # hostnamectl
    # Kernel version
    print("This is the Kernel version:")
    print(os.system("uname -a"))
    # uname -r
    # SetUID bits
    print("These are the SetUID bits:")
    print(os.system("find / -xdev \( -perm -4000 \) -type f -print0 | xargs -0 ls -l"))
    # SSH keys
    print("These are the SSH keys:")
    print(os.system("cat ~/.ssh/known_hosts"))
    # print(os.system("ls -al ~/.ssh"))
    # Cron Job for user "helpdesk"
    print("These are the cronjobs for helpdesk:")
    print(os.system("crontab -u helpdesk -l"))
    print("These are the cronjobs for root:")
    print(os.system("crontab -l"))
    # List running processes
    print("These are the running processes:")
    print(os.system("ps -A"))
    # Current sockets
    print("These are the sockets:")
    print(os.system("netstat -tulpn"))

def DELETE_LOGS():
    '''
    # The below command works for OS X, using the auth.log for test purposes
    try:
        os.system("sed -i '' -e '/127\.0\.0\.1/d' ./auth.log")
        print("127.0.0.1 has been deleted from ./auth.log")
    except:
        print("Error.")
        pass
    '''
    ip = input("Which IP would you like to delete from the system's logs? (e.g. 127.0.0.1): ")
    # ip = '127.0.0.1'
    # ip = '172.21.4.1'
    logs = input("Please specificy the logs, separated by commas, that you want to delete the IP from! (Default: auth.log, \"all\" specifies several logs) ")
    # logs = 'test'
    if logs == 'all':
        logs = "auth.log,kern.log,lastlog,messages,syslog,user.log"
        # cron.log,boot.log,mysql.log,vsftpd.log
    elif logs == '':
        logs = 'auth.log'
    # MAC OS X Testing
    elif logs == 'test':
        logs = 'test.log,testing.log'

    ip_split = ip.split(".")
    print(ip_split)
    logs_split = logs.split(",")
    print(logs_split)

    for log in logs_split:
        # Testing without file
        # command_tuple = "ls ", "-alh"
        # Testing with file
        # command_tuple = "cat ", log
        # MAC OS X
        # command_tuple = "sed -i '' -e \'/", ip_split[0], "\.", ip_split[1], "\.", ip_split[2], "\.", ip_split[3], "/d\' ", "/Users/stefanh/Downloads/python/CF/OS_Defensive/", log
        # Linux
        command_tuple = "sed -i \'/", ip_split[0], "\.", ip_split[1], "\.", ip_split[2], "\.", ip_split[3], "/d\' ", "/var/log/", log
        print(command_tuple)
        command = ''.join(command_tuple)
        print(command)
        os.system(command)
        print("All lines with \"{}\" have been deleted from {}.".format(ip,log))

FIND_CONFIGS()
# DELETE_LOGS()
