import getpass
import sys
import telnetlib
import time

HOST = input("Enter hostname: ")
user = input("Enter your remote account: ")
password = "cisco"

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: " ,3)
tn.write(user + "\n")
if password:
    tn.read_until(b"Password: ",3)
    tn.write(password + b"\n")

commands=["terminal length 0\n","show ip int br\n","show ip nat trans\n", \
"show run\n","show bgp ipv4 unicast summary\n","show bgp ipv6 unicast summary\n", \
"show pim neighbor\n","show mfib route summary\n","show platform\n","show redundancy\n", "show lacp\n"]

for command in commands:
	tn.write(command)

tn.write("exit\n")

filename = str(HOST) + "_" +time.strftime("%X")
with open( filename, "w") as out:
	out.write( tn.read_all())

