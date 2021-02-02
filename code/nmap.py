import socket
import threading
import time
import pyfiglet
import argparse
import platform
import os
import colorama
claen_window = lambda : os.system('clear') if platform.system().lower == 'linux' else os.system('cls')
def GetParmater():
    try:
        parser = argparse.ArgumentParser(description='Process Nmap Scan Port of device')
        parser.add_argument('-ip', '--ip', type=str, help='ipv4 Address')
        parser.add_argument('-max', '--max', type=int, help='max port of scan')

        args = parser.parse_args()
        return {'ip':args.ip, 'port':args.max}
    except:
        print(colorama.Fore.RED + 'missing ip, or max port' + colorama.Fore.RED)
        exit(404)

class nmap(object):
    def __init__(self):
        print(pyfiglet.figlet_format("Nmap Power"))
        self.MAX_THREAD = 500
        self.counter = 0
        self.desagin_value = "Port >> {0} service >> {1}"
    
    def ScanPort(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_port:
                socket_port.connect((ip, port))
                socket_port.settimeout(10)
                print(colorama.Fore.GREEN  + self.desagin_value.format(port, socket.getservbyport(port)) + colorama.Fore.GREEN )
                return True
        except:
            return False


    def __getitem__(self, data):
        for port in range(1, int(data['port'])):
            if self.counter == self.MAX_THREAD:
                self.counter = 0
                time.sleep(30)
            threading.Thread(target=self.ScanPort, args=(data['ip'], port)).start()
            self.counter += 1


if __name__ == '__main__':
    try:
        claen_window()
        parmater = GetParmater()
        obj = nmap()
        obj[parmater]
    except KeyboardInterrupt:
        print(colorama.Fore.RED + 'exit program' + colorama.Fore.RED)
        input('for exit process enter key...')