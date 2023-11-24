import re
import requests
import subprocess

def recognize_addr(devices):
    collected = []
    devices_tmp = []
    for i in devices:
        if len(i) > 0:
            response = subprocess.check_output("arp -a " + i) #checking ARP for MAC address


            out = re.findall("([0-9a-f]{2}(?:-[0-9a-f]{2}){5})", str(response)) #looking for MAC in string


            if len(out) == 1:
                api = "https://api.macvendors.com/" + out[0] #checking API for producer
                response = requests.get(api).text
                if response[0] == "{": #checking if call to API returned error
                    response = "Brak danych"
                collected.append("Adres IP: " + i + " Adres MAC: " + out[0] + " Producent: " + response) #building final message

    return collected