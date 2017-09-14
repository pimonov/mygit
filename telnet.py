import telnetlib
import time

user = input("Enter username: ")
passw = input("Enter password: ")
data = open('data.txt')
commands = 'sh run'
ter = 'terminal len 0'
ena = 'ena'

for line in data:
    tn = telnetlib.Telnet(line.rstrip())
    tn.set_debuglevel(1)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b'Password: ')
    tn.write(passw.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(ena.encode('ascii') + b"\n")
    tn.read_until(b'Password: ')
    tn.write(passw.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(ter.encode('ascii') + b"\n")
    time.sleep(2)
    tn.write(commands.encode('ascii') + b"\n")
    lastpost = tn.read_until(b"R#", timeout=2).decode('ascii')
    op = open("cisco.txt", "a").write(lastpost)
    tn.close()
