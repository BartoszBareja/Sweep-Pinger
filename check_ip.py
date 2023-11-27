import socket
import subprocess

def check_ips_in_range(start):
  host = socket.gethostbyname(socket.gethostname())[:-3] #getting the host subnet
  print(host)
  stop = start * 86 #declaring IP at which this sweep will end
  start = (start - 1) * 86 #declaring IP at which this sweep will start
  devices = [] #creating an array to
  for i in range(start, stop+1): # sweep pinging
    response = subprocess.call("ping -w 40 -n 1 " + host + "." + str(i))  # calling ping from CMD
    if response != 0 or str(i) == socket.gethostbyname(
            socket.gethostname()):  # if pinged IP is identical to host's don't add it into the array
      continue
    devices.append(host + "." + str(i))
  return devices