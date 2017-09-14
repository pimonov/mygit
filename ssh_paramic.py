import time
from datetime import datetime
import paramiko
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

file=open('devices.txt','r')
for line in file:
    timestamps = str(datetime.now())
    print('Timestamp: ', timestamps)
    info = {}
    info['ip'] = line.split(' ')[0]
    info['hostname'] = line.split(' ')[1]
    info['location'] = line.split(' ')[2]
    info['platform'] = line.split(' ')[3]

    def connector():

        ip_log = 'Connecting to IP: ' + info['ip']
        print(ip_log)

        hostname_log = 'With hostname: ' + info['hostname']
        print(hostname_log)

        location_log = 'From location: ' + info['location']
        print(location_log)

        client.connect(info['ip'], username='cisco', password='', timeout=5)

    try:
        connector()
        channel = client.invoke_shell()
        #channel.send('conf t\n')
        #channel.send('int fa0/0\n')
        #channel.send('description TEST_1\n')
        channel.send('wr\n')
        time.sleep(1)
        print('Done!\n')

    except Exception as e:
        error_log = str(e)
        print (error_log + '\n')

file.close()

