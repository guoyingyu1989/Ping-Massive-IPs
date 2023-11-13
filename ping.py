import os
import platform

def ping_ip(ip_address):
    try:
        if platform.system().lower()=="windows":
            response = os.system("ping -n 1 " + ip_address + " >nul 2>&1")
        else:
            response = os.system("ping -c 1 " + ip_address + " >/dev/null 2>&1")
        if response == 0:
            return ip_address + ' is up!'
        else:
            return ip_address + ' is down!'
    except Exception as e:
        return "An error occurred: " + str(e)
