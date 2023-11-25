import socket
import subprocess
import re
import requests
import multiprocessing
import tkinter as tk
from tkinter import ttk

from check_ip import check_ips_in_range #importing function to sweep ping
from recognize_addr import recognize_addr #importing function to search ARP and MAC API

host = socket.gethostbyname(socket.gethostname())[:-3]  # getting host IP


def main():
  devices = [] #defining array for IP's in network
  if __name__ == '__main__': #checking a function to avoid recursion
    with multiprocessing.Pool(processes=3) as pool:

      devices = pool.map(check_ips_in_range, [1,2,3]) #runing sweep ping in 3 separate batches to speed up the process

  #devices = [["192.168.5.1"], ["192.168.5.141"]]  # test data, used to save time in case of testing functions not related to pinging itself
  #devices = [['192.168.1.1', '192.168.1.100', '192.168.1.101', '192.168.1.103', '192.168.1.112']] # second set of test data
  devices_tmp = []

  for i in range(len(devices)): #loop to organize finding more than one IP in batch
    if len(devices[i]) > 0:
      tmp = devices[i]
      for ii in tmp:
        devices_tmp.append(ii)

  print(devices_tmp)

  devices = devices_tmp

  out = recognize_addr(devices) #searching ARP and calling MAC API

  print(out)

  main_window = tk.Tk()
  main_window.title("Sweep Pinger")

  table = tk.Frame(main_window)
  table.pack()

  table_mac = ttk.Treeview(table)

  table_mac['columns'] = ("id", "IP", "MAC", "Producer")

  table_mac.column("#0", width=0, stretch=tk.NO)
  table_mac.column("id", anchor=tk.CENTER, width=80)
  table_mac.column("IP", anchor=tk.CENTER, width=80)
  table_mac.column("MAC", anchor=tk.CENTER, width=80)
  table_mac.column("Producer", anchor=tk.CENTER, width=80)

  table_mac.heading("#0", text="", anchor=tk.CENTER)
  table_mac.heading("id", text="id", anchor=tk.CENTER)
  table_mac.heading("IP", text="IP", anchor=tk.CENTER)
  table_mac.heading("MAC", text="MAC", anchor=tk.CENTER)
  table_mac.heading("Producer", text="Producer", anchor=tk.CENTER)

  for i in range(len(out)):
    table_mac.insert(parent="",index = "end", iid = i +1, text = "", values = (i + 1, out[i][0], out[i][1], out[1][2]))


  table_mac.pack()
  main_window.mainloop()

main()