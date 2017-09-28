import getpass
import sys
import telnetlib
import time

HOST = '192.168.0.110'
user = 'admino'
password = "admino"

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: " ,3)
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ",3)
    tn.write(password.encode('ascii') + b"\n")

commands=["terminal length 0\n","show ip int br\n"]

for command in commands:
    tn.write(command.encode('ascii'))

tn.write(b"exit\n")

filename = str(HOST)

def write_in_file(lastpost):
    lastpost = tn.read_until(b'R#', timeout=2).decode('ascii')
    with open(filename, "w") as file:
        file.write(lastpost)
        tn.close()

