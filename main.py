import socket
import subprocess
import re
import requests
import multiprocessing

from check_ip import check_ips_in_range #importing function to sweep ping
from recognize_addr import recognize_addr #importing function to search ARP and MAC API

#devices = [["192.168.5.1"], ["192.168.5.141"]] # test data, used to save time in case of testing functions not related to pinging itslef

host = socket.gethostbyname(socket.gethostname())[:-3]  # getting host IP


def main():
  devices = [] #defining array for IP's in network
  if __name__ == '__main__': #checking a function to avoid recursion
    with multiprocessing.Pool(processes=3) as pool:

      devices = pool.map(check_ips_in_range, [1,2,3]) #runing sweep ping in 3 separate batches to speed up the process


  devices_tmp = []

  for i in range(len(devices)): #loop to organize finding more than one IP in batch
    if len(devices[i]) > 0:
      tmp = devices[i]
      for ii in tmp:
        devices_tmp.append(ii)

  print(devices_tmp)

  devices = devices_tmp

  out = recognize_addr(devices) #searching ARP and calling MAC API

  for i in out:
    print(i) #printing output

main()