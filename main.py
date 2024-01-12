import socket
import subprocess
import re
import requests
import multiprocessing
import tkinter as tk
from tkinter import ttk
from tkinter import *
import psutil

from check_ip import check_ips_in_range #importing function to sweep ping
from recognize_addr import recognize_addr #importing function to search ARP and MAC API
from network_interfaces import get_interfaces

host = "192.168.5.100"

def set_host(new_host):
  host = new_host

def get_host():
  return host

def main():
  devices = [] #defining array for IP's in network
  if __name__ == '__main__': #checking a function to avoid recursion

    addresses = psutil.net_if_addrs();

    main_window = tk.Tk()
    main_window.title("Sweep Pinger")
    table = tk.Frame(main_window)
    table.pack(expand=True, fill="both")

    interfaces = get_interfaces()

    print(interfaces)

    for interface in interfaces:
      button = tk.Button(text=str(interface[0]), command=lambda interface=interface: [main_window.destroy(), set_host(interface[1])]).pack()  # set_host(interface[1])).pack()


    main_window.mainloop()
    with multiprocessing.Pool(processes=3) as pool:

      devices = pool.starmap(check_ips_in_range, [(1, host),(2, host),(3, host)]) #runing sweep ping in 3 separate batches to speed up the process

      # devices = [["192.168.5.1"], ["192.168.5.141"]]  # test data, used to save time in case of testing functions not related to pinging itself
      # devices = [['192.168.1.1', '192.168.1.100', '192.168.1.101', '192.168.1.103', '192.168.1.112']] # second set of test data
      devices_tmp = []

    print(host)

    for i in range(len(devices)):  # loop to organize finding more than one IP in batch
      if len(devices[i]) > 0:
        tmp = devices[i]
        for ii in tmp:
          devices_tmp.append(ii)
    devices = devices_tmp



    out = recognize_addr(devices)  # searching ARP and calling MAC API

    main_window = tk.Tk()
    main_window.title("Sweep Pinger")
    table = tk.Frame(main_window)
    table.pack(expand=True, fill="both")

    table_mac = ttk.Treeview(table)

    table_mac['columns'] = ("id", "IP", "MAC", "Producer")

    table_mac.column("#0", width=0, stretch=tk.NO)
    table_mac.column("id", anchor=tk.CENTER, width=20)
    table_mac.column("IP", anchor=tk.CENTER, width=100)
    table_mac.column("MAC", anchor=tk.CENTER, width=100)
    table_mac.column("Producer", anchor=tk.CENTER, width=100)

    table_mac.heading("#0", text="", anchor=tk.CENTER)
    table_mac.heading("id", text="id", anchor=tk.CENTER)
    table_mac.heading("IP", text="IP", anchor=tk.CENTER)
    table_mac.heading("MAC", text="MAC", anchor=tk.CENTER)
    table_mac.heading("Producer", text="Producer", anchor=tk.CENTER)

    for i in range(len(out)):
      if len(out[i]) > 1:
        table_mac.insert(parent="", index="end", iid=i + 1, text="", values=(i + 1, out[i][0], out[i][1], out[i][2]))

    table_mac.pack(expand=True, fill="both")
    main_window.mainloop()


main()