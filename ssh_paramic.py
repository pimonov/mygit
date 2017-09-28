import paramiko
import netmiko
from netmiko import ConnectHandler
from getpass import getpass
import time
import re
import sys

# First ssh connection
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
print(output)

# Second SSH connection
remote_conn.send("ssh ver \n>")
time.sleep(3)
remote_conn.send("password\n")
output1 = remote_conn.recv(65535)
print(output1)
time.sleep(3)

# Trying to run netmiko...
net_connect = ConnectHandler(device_type='cisco_ios', ip='x.x.x.x', username='user', password='password')
net_connect.find_prompt()

CISCO_SHOW_ACL_x = net_connect.send_command("show run | s access-list x ")
